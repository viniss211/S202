CREATE (:Homem:advogado{nome:'Marcus',sexo:"masculino",idade:'41'})
CREATE(:Mulher:Assistente_de_qualidade{nome:'Flavia',sexo:"feminino",idade:'40'})
CREATE(:Mulher:Fotografa{nome:'Juscelena',sexo:"feminino",idade:'66'})
CREATE(:Homem:Estagiário_de_desenvolvimento{nome:'Vinícius',sexo:"masculino",idade:'21'})
CREATE(:Homem:Desenvolvedor_de_Embarcados{nome:'Thiago',sexo:"masculino",idade:'35'})
CREATE(:Mulher:Engenheira_de_telecomunicacao{nome:'Marina',sexo:"feminino",idade:'30'})
CREATE(:Homem:Vendedor{nome:'Flavio',sexo:"masculino",idade:'44'})
CREATE(:Mulher:aposentada{nome:'Cristina',sexo:"feminino",idade:'70'})
CREATE(:Mulher:vendedora{nome:'Yasmim',sexo:"feminino",idade:'23'})
CREATE(:Homem:Lavador{nome:'Icaro',sexo:"Masculino",idade:'27'})

MATCH (m:Mulher:Assistente_de_qualidade{nome:'Flavia',sexo:"feminino",idade:'40'}), (f:Homem:Estagiário_de_desenvolvimento{nome:'Vinícius'})
CREATE (m)-[:PAI_DE]->(f)

MATCH (p:Homem:advogado{nome:'Marcus',sexo:"masculino",idade:'41'}), (f:Homem:Estagiário_de_desenvolvimento{nome:'Vinícius',sexo:"masculino",idade:'21'})
CREATE (p)-[:PAI_DE]->(f)

MATCH (v:{nome:'Marina'}), (f:{nome:'Vinícius'})
CREATE (v)-[:TIO_DE]->(f)

MATCH (v:{nome:'Thiago'}), (f:{nome:'Vinícius'})
CREATE (v)-[:TIO_DE]->(f)

MATCH (v:{nome:'Thiago'}), (f:{nome:'Marina'})
CREATE (v)-[:IRMAO_DE]->(f)

MATCH (v:{nome:'Marina'}), (f:{nome:'Marcus'})
CREATE (v)-[:IRMAO_DE]->(f)

MATCH (v:{nome:'Cristina'}), (f:{nome:'Marina'})
CREATE (v)-[:PAI_DE]->(f)

MATCH (v:{nome:'Cristina'}), (f:{nome:'Marcus'})
CREATE (v)-[:PAI_DE]->(f)

MATCH (v:{nome:'Cristina'}), (f:{nome:'Vinícius'})
CREATE (v)-[:AVO_DE]->(f)

MATCH (v:{nome:'Cristina'}), (f:{nome:'THIAGO'})
CREATE (v)-[:PAI_DE]->(f)

MATCH (v:{nome:'Thiago'}), (f:{nome:'Marcus'})
CREATE (v)-[:IRMAO_DE]->(f)

MATCH (v:Mulher{nome:'Juscelena'}), (f:{nome:'Vinícius'})
CREATE (v)-[:AVO_DE]->(f)

MATCH (v:Mulher{nome:'Juscelena'}), (f:{nome:'Icaro'})
CREATE (v)-[:AVO_DE]->(f)

MATCH (v:Mulher{nome:'Juscelena'}), (f:{nome:'Yasmim'})
CREATE (v)-[:AVO_DE]->(f)

MATCH (v:Mulher{nome:'Juscelena'}), (f:{nome:'Flávia'})
CREATE (v)-[:PAI_DE]->(f)

MATCH (v:{nome:'Flávia'}), (f:{nome:'Flavio'})
CREATE (v)-[:IRMAO_DE]->(f)

MATCH (v:{nome:'Flávia'}), (f:{nome:'Icaro'})
CREATE (v)-[:TIO_DE]->(f)

MATCH (v:{nome:'Flavio'}), (f:{nome:'Yasmim'})
CREATE (v)-[:PAI_DE]->(f)

MATCH (v:{nome:'Flavio'}), (f:{nome:'Icaro'})
CREATE (v)-[:PAI_DE]->(f)

MATCH (v:{nome:'Yasmim'}), (f:{nome:'Icaro'})
CREATE (v)-[:IRMAO_DE]->(f)

MATCH (v:{nome:'Flávia'}), (f:{nome:'Yasmim'})
CREATE (v)-[:TIO_DE]->(f)
