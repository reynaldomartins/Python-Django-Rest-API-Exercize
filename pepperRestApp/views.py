import json
from django.forms.models import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from .models import TODOs, TodoStates
from .serializers import TODOSerializer
from rest_framework.response import Response
from rest_framework.views import status
from datetime import datetime
from django.db.models import Q

# Serializers views

class TODOsBasicAPIView(generics.ListCreateAPIView):
    # the declarations bellow are used for GET method which will return all TODOs
    # It is not necessary to declare get method here
    queryset = TODOs.objects.all()
    serializer_class = TODOSerializer

    def post(self, request, *args, **kwargs):
        # In view, data is received already as a converted object format used by Python, not as Json
        global TodoStates
        data = request.data
        data_dict_list = []
        if isinstance( data, dict ):
            data_dict_list.append(data)
        elif isinstance( data, list ):
            data_dict_list = data
        else:
            return Response(
                data={
                    "message": "The Data Params informed are not in a proper format. See API documentation."
                },
                status=status.HTTP_422_UNPROCESSABLE_ENTITY )
        try:
            list_newtodo = []
            for todo in data_dict_list:
                if isinstance( todo, dict ):
                    if not todo["td_state"] in TodoStates:
                        print("Not valid state")
                        return Response(
                            data={
                                "message": "The state : {} informed does not exist. One or more TODOs could not have been created before.".format(todo["td_state"])}
                            ,
                            status=status.HTTP_422_UNPROCESSABLE_ENTITY
                            )
                    newtodo = TODOs.objects.create(
                        td_state=todo["td_state"],
                        td_duedate=todo["td_duedate"],
                        td_text=todo["td_text"])
                    list_newtodo.append(newtodo)
                else:
                    return Response(
                        data={
                            "message": "The Data Params informed could not be in a proper format. One or more TODOs could have been added before. See API documentation."
                        },
                        status=status.HTTP_422_UNPROCESSABLE_ENTITY )
            return Response(
                data=TODOSerializer(list_newtodo,many=True).data,
                status=status.HTTP_201_CREATED
            )
        except:
            return Response(
                data = { "message" : "It was not possible to proceed with TODO creation request" },
                status=status.HTTP_400_BAD_REQUEST
            )

class TODOsIDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TODOs.objects.all()
    serializer_class = TODOSerializer

    def get(self, request, *args, **kwargs):
        try:
            todo = self.queryset.get(pk=kwargs["pk"])
            print("here")
            return Response(TODOSerializer(todo).data)
        except:
            return Response(
                data={
                    "message": "TODO with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def put(self, request, *args, **kwargs):
        # In view, data is received already as a converted object format used by Python, not as Json
        data = request.data
        pk=kwargs["pk"]
        # print("data {}".format(data))
        # print("pk {}".format(pk))
        if not isinstance( data, dict ):
            return Response(
                data={
                    "message": "The Data Params informed are not in a proper format. See API documentation."
                },
                status=status.HTTP_422_UNPROCESSABLE_ENTITY )
        try:
            try:
                todo = self.queryset.get(pk=pk)
            except:
                return Response(
                    data={
                        "message": "TODO with id: {} does not exist.".format(pk)
                    },
                    status=status.HTTP_422_UNPROCESSABLE_ENTITY )
            else:
                # print("todo {}".format(todo))
                todo.td_state = data["td_state"]
                todo.td_duedate = data["td_duedate"]
                todo.td_text = data["td_text"]
                todo.save()
                return Response(
                    data=TODOSerializer(todo).data,
                    status=status.HTTP_202_ACCEPTED
                )
        except:
            return Response(
                data = { "message" : "It was not possible to proceed with TODO update request." },
                status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, *args, **kwargs):
        if request.data:
            try:
                data_list = request.data
                if not isinstance( data_list, list ):
                    return Response(
                        data={
                            "message": "The Data Params informed are not in a proper format. See API documentation."
                        },
                        status=status.HTTP_422_UNPROCESSABLE_ENTITY )
                else:
                    for pk in data_list:
                        try:
                            todo = self.queryset.get(pk=pk)
                        except:
                            return Response(
                                data={
                                    "message": "TODO with id: {} does not exist. One or more TODOs could have been deleted before.".format(pk)
                                },
                                status=status.HTTP_422_UNPROCESSABLE_ENTITY
                            )
                        else:
                            todo.delete()
                    return Response(data = {
                                    "message": "TODO(s) with id(s): {} were deleted as per your request".format(data_list)
                                },
                                status=status.HTTP_202_ACCEPTED)
            except:
                 return Response(
                     data = { "message" : "It was not possible to proceed with TODO update request." },
                     status=status.HTTP_400_BAD_REQUEST
                 )
        else:
            pk=kwargs["pk"]
            try:
                todo = self.queryset.get(pk=pk)
            except:
                return Response(
                    data={
                        "message": "TODO with id: {} does not exist".format(kwargs["pk"])
                    },
                    status=status.HTTP_422_UNPROCESSABLE_ENTITY
                )
            else:
                try:
                    todo.delete()
                    return Response(data = {
                                    "message": "TODO with id: {} was deleted as per your request".format(kwargs["pk"])
                                },
                                status=status.HTTP_202_ACCEPTED)
                except:
                     return Response(
                         data = { "message" : "It was not possible to proceed with TODO update request." },
                         status=status.HTTP_400_BAD_REQUEST
                     )

class TODOsFilterDuedateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TODOs.objects.all()
    serializer_class = TODOSerializer

    def get(self, request, *args, **kwargs):
        td_duedate_str=kwargs["td_duedate"]
        try:
            td_duedate = datetime.strptime(td_duedate_str, '%Y-%m-%d')
        except:
            return Response(
                data={
                    "message": "Duedate: {} informed is not in a valid format. See API Documentation.".format(kwargs["td_duedate"])
                },
                status=status.HTTP_404_NOT_FOUND
            )
        else:
            qs_todo = self.queryset.filter(td_duedate=td_duedate)
            if qs_todo:
                return Response(TODOSerializer(qs_todo,many=True).data)
            else:
                return Response(
                    data={
                        "message": "TODO with duedate: {} does not exist".format(kwargs["td_duedate"])
                    },
                    status=status.HTTP_404_NOT_FOUND
                )

class TODOsFilterStateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TODOs.objects.all()
    serializer_class = TODOSerializer

    def get(self, request, *args, **kwargs):
        td_state = kwargs["td_state"]
        if not td_state in TodoStates:
            return Response(
                data={
                    "message": "The state : {} searched does not exist".format(td_state)
                },
                status=status.HTTP_404_NOT_FOUND
            )
        qs_todo = self.queryset.filter(td_state=td_state)
        if qs_todo:
            return Response(TODOSerializer(qs_todo, many=True).data)
        else:
            return Response(
                data={
                    "message": "There isn't any TODO with the state : {}".format(td_state)
                },
                status=status.HTTP_404_NOT_FOUND
        )

class TODOsFilterStateDuedateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TODOs.objects.all()
    serializer_class = TODOSerializer

    def get(self, request, *args, **kwargs):
        oper = kwargs['oper']
        td_state = kwargs["td_state"]
        if not td_state in TodoStates and oper == "and":
            return Response(
                data={
                    "message": "The TODO state {} searched does not exist".format(td_state)
                },
                status=status.HTTP_404_NOT_FOUND
            )
        td_duedate_str=kwargs["td_duedate"]
        td_duedate = datetime.strptime(td_duedate_str, '%Y-%m-%d')

        if oper == "and":
            qs_todo = self.queryset.filter(td_state=td_state, td_duedate=td_duedate)
        elif oper == "or":
            qs_todo = self.queryset.filter(Q(td_state=td_state) | Q(td_duedate=td_duedate))
        else:
            return Response(
                data={
                    "message": "Operator : {} is not permited".format(oper)
                },
                status=status.HTTP_404_NOT_FOUND
            )

        if qs_todo:
            return Response(TODOSerializer(qs_todo,many=True).data)
        else:
            return Response(
                data={
                    "message": "TODO with state : {} {} duedate: {} does not exist".format(td_state,oper, td_duedate_str)
                },
                status=status.HTTP_404_NOT_FOUND
            )
