# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
from typing import Any, Text, Dict, List  #pe of data
from rasa_sdk import Action, Tracker   #custom action and tracker the data
from rasa_sdk.events import SlotSet, SessionStarted, ActionExecuted, EventType  #fill the slote
from rasa_sdk import Tracker, FormValidationAction
#连接图数据库
from py2neo import Node, Relationship, Graph, NodeMatcher, RelationshipMatcher

class ActionProvince(Action):

  def name(self) -> Text:
     return "action_province"    #return the name

  async def run(
      self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
  ) -> List[Dict[Text, Any]]:
#" Collect slots"
    value = tracker.get_slot("province")
    dispatcher.utter_message(text="Hello World!")
    print("1")
    return [SlotSet(value)]

class ActionCourse(Action):

  def name(self) -> Text:
     return "action_course"    #return the name

  async def run(
      self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
  ) -> List[Dict[Text, Any]]:
#" Collect slots"
    value = tracker.get_slot("course")
    dispatcher.utter_message(text="Hello World!")
    print("1")
    return [SlotSet(value)]


# class ActionRecruitment(Action):
#
#     def name(self) -> Text:
#         return "action_recruitment"  # return the name
#
#     # # #查询节点是否存在,根据节点的标签和节点的属性查询节点是否存在
#     # def MatchNode(m_graph, m_label, m_attrs):
#     #     m_n = "_.name=" + "\'" + m_attrs['name'] + "\'"
#     #     matcher = NodeMatcher(m_graph)  # 查询之前都要获得一个查询标签
#     #     re_value = matcher.match(m_label).where(m_n).first()
#
#     async def run(
#             self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
#     ) -> List[Dict[Text, Any]]:
#         # " Collect slots"
#         value1 = tracker.get_slot("province")
#         value2 = tracker.get_slot("typecourse")
#         dispatcher.utter_message(text="Hello World!" + value1 + value2)
#         return [SlotSet(value1)]
#         # dispatcher.utter_message(text="Hello World!")
#         # print("1")
#         # return [SlotSet(value)]


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
