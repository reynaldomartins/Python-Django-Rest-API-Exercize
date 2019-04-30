import json
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import TODOs
from .serializers import TODOSerializer
from datetime import datetime, timedelta
from django.db.models import Q

def print_response(response):
    print("Returned from the REST API. Code = '{}'', Data = '{}''".format(response.status_code, response.data))

class UpdateTodoDBTestCases(APITestCase):
    client = APIClient()

    def add_todo_post(self, **kwargs):
        # Convert data in dict format to Json before call the POST method
        data_jason = json.dumps(kwargs["data"])
        return self.client.post(
            reverse(
                "todos_basic_api_method",
                kwargs={
                    "version": "v1"
                }
            ),
            data=data_jason,
            content_type='application/json'
        )

    def setUp(self):
        # One TODO creation test case
        td_duedate_iso = (datetime.now().date()+timedelta(days=19)).isoformat()
        data_dict = {
            "td_state" : "T",
            "td_duedate" : td_duedate_iso,
            "td_text" : "Sales Meeting",
        }
        self.add_todo_post(data=data_dict)

        # Multiple TODO creation test case
        td_duedate_iso = (datetime.now().date()+timedelta(days=-5)).isoformat()
        td_duedate_iso2 = (datetime.now().date()+timedelta(days=-10)).isoformat()
        td_duedate_iso3 = (datetime.now().date()+timedelta(days=40)).isoformat()
        data_dict_list = [{ "td_state" : "I","td_duedate" : td_duedate_iso,"td_text" : "Lecturer"},
                     { "td_state" : "D","td_duedate" : td_duedate_iso2,"td_text" : "Code Review"},
                     { "td_state" : "T","td_duedate" : td_duedate_iso3,"td_text" : "New Product Development"}]
        self.add_todo_post(data=data_dict_list)

        queryset = TODOs.objects.all()
        print("\n\n*** New Test Case - DB Create = {}".format(queryset))

    def update_todo_put(self, pk=0, data=[]):
        # Convert data in dict format to Json before call the POST method
        data_jason = json.dumps(data)
        return self.client.put(
            reverse(
                "todos_id_api_method",
                kwargs={
                    "version": "v1",
                    "pk" : pk
                }
            ),
            data=data_jason,
            content_type='application/json'
        )

    def test_put(self):
        print("\n#### Entering Update/PUT Test Case")
        td_duedate_iso = (datetime.now().date()+timedelta(days=40)).isoformat()
        data_dict = {
            "td_state" : "I",
            "td_duedate" : td_duedate_iso,
            "td_text" : "Sales Meeting - postponed",
        }
        response = self.update_todo_put(1,data_dict)
        print_response(response)

        # wrong case, id does not exist
        response = self.update_todo_put(9,data_dict)
        print_response(response)

        # wrong case, wrong format
        data_dict = 5
        response = self.update_todo_put(1,data_dict)
        print_response(response)

        queryset = TODOs.objects.all()
        print("DB After AFTER wrong Additions - {}".format(queryset))


    def test_creation_wrong(self):
        print("\n#### Entering ADD/POST - with Wrong Data - Test Case")
        # Wrong Params input TODO creation test cases
        # Wrong todo dict entry
        print("DB size BEFORE wrong Additions = {}".format(TODOs.objects.all().count()))
        td_duedate_iso = (datetime.now().date()+timedelta(days=-20)).isoformat()
        data_dict_list = [{ "td_state" : "I","td_duedate" : td_duedate_iso,"td_text" : "Training"},
                    5 ]
        response = self.add_todo_post(data=data_dict_list)
        print_response(response)

        # Wrong todo list entry
        data_dict_list = 5
        response = self.add_todo_post(data=data_dict_list)
        print_response(response)
        queryset = TODOs.objects.all()
        print("DB size AFTER wrong Additions = {}".format(queryset.count()))
        print("DB After AFTER wrong Additions - {}".format(queryset))

    def delete_todo_delete(self, pk=0, data=[]):
        if pk == 0:
            if data != []:
                data_jason = json.dumps(data)
                return self.client.delete(
                    reverse(
                        "todos_id_api_method",
                        kwargs={
                            "version": "v1",
                            "pk": 0
                        }),
                        data=data_jason,
                        content_type='application/json'
                )
            else:
                return
        else:
            return self.client.delete(
                reverse(
                    "todos_id_api_method",
                    kwargs={
                        "version": "v1",
                        "pk": pk
                    }
                )
            )
        print_response(response)
        return response

    def test_deletes(self):
        print("\n#### Entering Delete/DELETE Test Case")
        print("DB size BEFORE deletions = {}".format(TODOs.objects.all().count()))
        response = self.delete_todo_delete(pk=1)
        print_response(response)
        response = self.delete_todo_delete(pk=9)
        print_response(response)
        queryset = TODOs.objects.all()
        print("DB After SINGLE deletion - {}".format(queryset))
        print("DB size After SINGLE deletions = {}".format(queryset.count()))

        pk_list = [ 3, 4 ]
        response = self.delete_todo_delete(data=pk_list)
        print_response(response)
        pk_list = 5
        response = self.delete_todo_delete(data=pk_list)
        print_response(response)
        pk_list = [ { "foo" : 1000 } ]
        response = self.delete_todo_delete(data=pk_list)
        print_response(response)
        print("DB After MULTIPLE deletion - {}".format(queryset))
        print("DB size After MULTIPLE deletions = {}".format(queryset.count()))

    def test_list_all_todos(self):
        print("\n#### Entering Get All/GET Test Case")
        response = self.client.get(
            reverse("todos_basic_api_method",kwargs={"version": "v1"})
        )
        print_response(response)
        qs_todo = TODOs.objects.all()
        serialized = TODOSerializer(qs_todo, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_todo_by_pk(self):
        print("\n#### Entering Get by Id/GET Test Case")
        self.get_todo_by_pk(1)
        self.get_todo_by_pk(2)
        self.get_todo_by_pk(3)
        # Testing a wrong primary key
        # self.get_todo_by_pk(4)

    def get_todo_by_pk(self,pk):
        response = self.client.get(
            reverse("todos_id_api_method",kwargs={"version": "v1", "pk": pk})
        )
        print_response(response)
        todo = TODOs.objects.get(pk=pk)
        serialized = TODOSerializer(todo)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_todos_by_filterstate(self):
        print("\n#### Entering Filtered by State/GET Test Case")
        self.get_todos_by_filterstate("T")
        self.get_todos_by_filterstate("D")
        self.get_todos_by_filterstate("I")
        # Testing a wrong state
        self.get_todos_by_filterstate("Z")

    def get_todos_by_filterstate(self,td_state):
        response = self.client.get(
            reverse("todos_filterstate_api_method",kwargs={"version": "v1", "td_state": td_state})
        )
        print_response(response)
        qs_todo = TODOs.objects.all().filter(td_state=td_state)
        serialized = TODOSerializer(qs_todo, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_todos_by_filterduedate(self):
        print("\n#### Entering Filtered by DueDate/GET Test Case")
        self.get_todos_by_filterduedate((datetime.now().date()+timedelta(days=-5)).isoformat())
        self.get_todos_by_filterduedate((datetime.now().date()+timedelta(days=-10)).isoformat())
        # Testing a wrong date
        self.get_todos_by_filterduedate("2019-12-31")

    def get_todos_by_filterduedate(self,td_duedate):
        response = self.client.get(
            reverse("todos_filterduedate_api_method",kwargs={"version": "v1", "td_duedate": td_duedate})
        )
        print_response(response)
        qs_todo = TODOs.objects.all().filter(td_duedate=td_duedate)
        serialized = TODOSerializer(qs_todo, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_todos_by_filterstateduedate(self):
        print("\n#### Entering Search by State and/or DueDate/GET Test Case")
        self.get_todos_by_filterstateduedate("T","and",(datetime.now().date()+timedelta(days=-5)).isoformat())
        self.get_todos_by_filterstateduedate("I","and",(datetime.now().date()+timedelta(days=-5)).isoformat())
        self.get_todos_by_filterstateduedate("D","and",(datetime.now().date()+timedelta(days=-5)).isoformat())
        self.get_todos_by_filterstateduedate("T","or",(datetime.now().date()+timedelta(days=-10)).isoformat())
        self.get_todos_by_filterstateduedate("I","or",(datetime.now().date()+timedelta(days=-10)).isoformat())
        self.get_todos_by_filterstateduedate("D","or",(datetime.now().date()+timedelta(days=-10)).isoformat())

    def get_todos_by_filterstateduedate(self, td_state, oper, td_duedate):
        response = self.client.get(
            reverse("todos_filterstateduedate_api_method",kwargs={"version": "v1", "td_state" :td_state, "oper" : oper ,"td_duedate": td_duedate,})
        )
        print_response(response)
        if oper == "and":
            qs_todo = TODOs.objects.all().filter(td_state=td_state, td_duedate=td_duedate)
        elif oper == "or":
            qs_todo = TODOs.objects.all().filter(Q(td_state=td_state) | Q(td_duedate=td_duedate))
        else:
            qs_todo = []
        serialized = TODOSerializer(qs_todo, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
