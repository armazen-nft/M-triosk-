MERGE (e1200:Era {id: "1200_latim"})
  SET e1200.label = "Europa Medieval";
MERGE (e1700:Era {id: "1700_portugues"})
  SET e1700.label = "Período Colonial";
MERGE (e1960:Era {id: "1960_ingles"})
  SET e1960.label = "Modernidade Tardia";

MERGE (m:Modulo {name: "integracao_temporal"})
MERGE (m)-[:CONTEXTUALIZA]->(e1200)
MERGE (m)-[:CONTEXTUALIZA]->(e1700)
MERGE (m)-[:CONTEXTUALIZA]->(e1960);
