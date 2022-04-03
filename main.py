from eliza.eliza import Eliza


if __name__=="__main__":
  therapist = Eliza(lang="es")
  print('Say "quit" to finish conversation')
  query = ""
  while query not in ["quit","adios"]:
    query = input("User: ")
    print(f"Eliza: {therapist.respond(query)}")