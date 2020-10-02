#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
  """
  YOUR CODE HERE
  """
  route = []
  
  route = plezWork(tickets, length, [])
              
  return route

def plezWork(tickets, length, newRoute):
  length -= 1
  count = 0

  if length == 0:
      newRoute.append(tickets[0].destination)
      return newRoute

  else:
      for i in tickets:
          if len(newRoute) == 0:
            if i.source == "NONE":
              print(i.source)
              newRoute.append(i.destination)
              tickets.pop(count)
              plezWork(tickets, length, newRoute)
            
            
          elif i.source == newRoute[-1]:
            print(i.source)
            newRoute.append(i.destination)
            tickets.pop(count)
            plezWork(tickets, length, newRoute)

            
          count += 1
          #   return plezWork(tickets, length, newRoute)
          
          # if i.source == tickets[-1]:
          #    tickets.remove(i)

  return newRoute


ticket_1 = Ticket("PIT", "ORD")
ticket_2 = Ticket("XNA", "SAP")
ticket_3 = Ticket("SFO", "BHM")
ticket_4 = Ticket("FLG", "XNA")
ticket_5 = Ticket("NONE", "LAX")
ticket_6 = Ticket("LAX", "SFO")
ticket_7 = Ticket("SAP", "SLC")
ticket_8 = Ticket("ORD", "NONE")
ticket_9 = Ticket("SLC", "PIT")
ticket_10 = Ticket("BHM", "FLG")

tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5,
ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]

expected = ["LAX", "SFO", "BHM", "FLG", "XNA", "SAP",
"SLC", "PIT", "ORD", "NONE"]
result = reconstruct_trip(tickets, 10)

print(result)