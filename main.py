from eliza.eliza import Eliza


if __name__=="__main__":
  therapist = Eliza()
  query = ""
  while query!="quit":
    query = input("User: ")
    print(f"Eliza: {therapist.respond(query)}")