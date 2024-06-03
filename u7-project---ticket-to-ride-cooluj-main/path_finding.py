from math import sqrt
import sys
from typing import Dict, List, Set, Tuple
from priority_queue import PriorityQueue
# You do not need to change this class.  It is used as the return type for get_minimum_path
class RouteInfo:
   def __init__(self,
                route: List[Tuple[str, str]], # list of tuples of friendly names for the start and destination cities
                route_ids: List[Tuple[int, int]], # list of tuples of ids for the start and destination cities
                cost: int) -> None: # the total cost of the route from start to destination
       self.route = route
       self.route_ids = route_ids
       self.cost = cost
# TODO: Implement the methods on the PathFinder class using an underlying graph representation
# of your choice. Feel free to use your graph classes from the practice exercises; copy the appropriate
# files into your project and import the classes at the top of this file.
class PathFinder:
   def __init__(self) -> None:
        #pass
        # add 2 members to track city and its neighbors
        self.city = {}
        self.neighbors = {}
   
   # [DONE] TODO: adds an edge to the graph, using a the id of the start node and id of the finish node
   def add_edge(self, start_id: int, finish_id:int , cost: float) -> None:
       if start_id not in self.neighbors:
           self.neighbors[start_id] = []
     
       self.neighbors[start_id].append((finish_id,cost))
   
   # [DONE] TODO: adds a node to the graph, passing in the id, friendly name, and location of the node.
   # location is a tuple with the x and y coordinates of the location
   def add_node(self, id: int, name: str, location: Tuple[float, float]) -> None:
       self.city[id] = City(name, location)
   
   # TODO: calculates the minimum path using the id of the start city and id of the destination city, using A*
   # Returns a RouteInfo object that contains the edges for the route.  See RouteInfo above for attributes
   # Note: This implementation should use A*.  Tests that should pass

   #I got help from Lucky, Sam, Vaibahv with this portion of the code
   def get_minimum_path(self, start_city_id: int, destination_id:int ) -> RouteInfo:
       # variable to store the cities visited in order to avoid visiting it again
       visited_city = set() 
       
       nextcity_queue = PriorityQueue()
       # enqueue the initial path (cost 0) to th priority queue
       nextcity_queue.enqueue(self.heuristic(start_city_id, destination_id), RouteInfo([], [], 0)) 
       
       # while next city queue is not empty select the city with the lowest cost
       while not nextcity_queue.is_empty():
           path_to_be_visited = nextcity_queue.dequeue() 
           
           # tracks the current city in the path
           current_city = start_city_id # represents where we are in the path
           if len(path_to_be_visited.route_ids) > 0:
               current_city = path_to_be_visited.route_ids[len(path_to_be_visited.route_ids) - 1][1]
               
           # if the current city is the destination city, the shortest path has been found
           if current_city == destination_id: 
               return path_to_be_visited 
           
           # if the current city is not the destination
           if current_city not in visited_city and current_city in self.neighbors:
               current_neighbors = self.neighbors[current_city]
               
               # generate its neighboring cities
               for (neighbor, cost) in current_neighbors:
                   if neighbor in visited_city:
                       continue
                   # for each neighboring city, calculate the cost to reach that city from start city
                   revised_cost = path_to_be_visited.cost + cost 
                   revised_route_ids = path_to_be_visited.route_ids + [(current_city, neighbor)] 
                   city_name = self.city[current_city].name
                   neighbor_city_name = self.city[neighbor].name
                   revised_route = path_to_be_visited.route + [(city_name, neighbor_city_name)]
                   revised_path = RouteInfo(revised_route, revised_route_ids, revised_cost)
                   nextcity_queue.enqueue(revised_cost + self.heuristic(neighbor, destination_id), revised_path)
           # mark the current city as visited          
           visited_city.add(current_city)
     
       return None

   # this heuristic function provides an estimate of the remaining distance from a given city to the destination city
   # this function uses a straight-line distance as heuristic using the 2 dimensional location coordinates
   def heuristic(self, city_id: int, destination_id: int) -> float:
       # use the distance formulae Square root of ((X1-X2)**2 + (Y1-Y2)**2)
       return ((self.city[city_id].location[0] - self.city[destination_id].location[0]) ** 2 + (self.city[city_id].location[1] - self.city[destination_id].location[1]) ** 2)**0.5

# implementing a new class to holding city name and location
class City:
   def __init__(self, name: str, location: Tuple[float, float]) -> None:
       self.name = name
       self.location = location

