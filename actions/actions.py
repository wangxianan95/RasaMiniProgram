# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
from typing import Any, Text, Dict, List  #pe of data
from rasa_sdk import Action, Tracker   #custom action and tracker the data
from rasa_sdk.events import SlotSet, SessionStarted, ActionExecuted, EventType  #fill the slote
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


class ActionRecruitment(Action):

    def name(self) -> Text:
        return "action_recruitment"  # return the name

    def MatchNode(self, m_graph, m_label, m_attrs, m_label2, m_attrs2, typecourse):
        m_n1 = "_.name=" + "\'" + m_attrs['name'] + "\'"
        m_n2 = "_.name=" + "\'" + m_attrs2['name'] + "\'"
        matcher = NodeMatcher(m_graph)
        re_value1 = matcher.match(m_label).where(m_n1).first()
        re_value2 = matcher.match(m_label2).where(m_n2).first()
        # 查询
        relationship_matcher = RelationshipMatcher(m_graph)
        relationship = list(relationship_matcher.match((re_value2, re_value1), r_type=typecourse))
        return relationship

    async def run(
            self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        graph = Graph('http://localhost:7474/', auth=("neo4j", "lyt"))
        # " Collect slots"
        value1 = tracker.get_slot("province")
        value2 = tracker.get_slot("major")
        value3 = tracker.get_slot("typecourse")
        label1 = 'Province'
        attrs1 = {"name": value1}
        label2 = 'Major'
        attrs2 = {"name": value2}
        typecourse = 'Science'
        if value3 == '理科' or value3 == '理科生':
            typecourse = 'Science'
        elif value3 == '文科' or value3 == '文科生':
            typecourse = 'Art'
        elif value3 == '新高考地区' or value3 == '新高考':
            typecourse = 'Fix'
        value = self.MatchNode(graph, label1, attrs1, label2, attrs2,typecourse)
        valueget1 = value[0].get('minOrder1')
        valueget2 = value[0].get('minOrder2')
        valueget3 = value[0].get('minOrder3')
        if value[0].get('minOrder1') == None:
            valueget1 = '无'
        elif value[0].get('minOrder2') == None:
            valueget2 = '无'
        elif value[0].get('minOrder3') == None:
            valueget3 = '无'
        dispatcher.utter_message(text=value3 + ":" + value2 + "在" + value1 + "2018-2020的最低分数线排名为" + valueget1
                                 + " , " + valueget2 + " , " + valueget3)
        print("1")
        return []
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
