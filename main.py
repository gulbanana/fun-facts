from simplesqlite import SimpleSQLite

con = SimpleSQLite("facts.sqlite", "w")

con.create_table("Fact", ["Datum", "IsFun"])
con.insert("Fact", {"Datum": "All dogs go to heaven.", "IsFun": True})
con.insert("Fact", {"Datum": "1 + 1 = 2.", "IsFun": False})

for record in con.select("Datum", "Fact", "IsFun = 'True'"):
    print(record[0])
