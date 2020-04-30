SELECT DISTINCTROW [Nome] & " " & [Sobrenome] AS NomeP, [Pacientes por Sobrenome].ID, [Endereço] & ", " & [Endnum] & " / " & [EndApart] AS EndP, [Pacientes por Sobrenome].CEP, [Pacientes por Sobrenome].Cidade, Procedimentos.Data
FROM [Pacientes por Sobrenome] INNER JOIN Procedimentos ON [Pacientes por Sobrenome].ID = Procedimentos.[ID da Paciente]
WHERE (((Procedimentos.Data) Like Aviso_renovar([Data],[Renovar])))
ORDER BY [Nome] & " " & [Sobrenome]
WITH OWNERACCESS OPTION;

SELECT DISTINCTROW [Nome] & " " & [Sobrenome] AS NomeP, [Pacientes por Sobrenome].ID, [Endereço] & ", " & [Endnum] & " / " & [EndApart] AS EndP, [Pacientes por Sobrenome].CEP, [Pacientes por Sobrenome].Cidade, [Pacientes por Sobrenome].ID AS Cont, Procedimentos.Data
FROM [Pacientes por Sobrenome] INNER JOIN Procedimentos ON [Pacientes por Sobrenome].ID = Procedimentos.[ID da Paciente]
WHERE (((Aviso_renovar([Data],[Renovar]))=1))
ORDER BY [Nome] & " " & [Sobrenome]
WITH OWNERACCESS OPTION;

SELECT DISTINCTROW pacientes.*
FROM pacientes
ORDER BY pacientes.Sobrenome, pacientes.Nome
WITH OWNERACCESS OPTION;

SELECT DISTINCTROW [Tabela de Lembretes].[Título do Lembrete], [Tabela de Lembretes].[Descrição do Lembrete]
FROM [Tabela de Lembretes]
ORDER BY [Tabela de Lembretes].[Título do Lembrete];

SELECT DISTINCTROW [Tabela de Prescrições].[Título da Prescrição], [Tabela de Prescrições].[Descrição da Prescrição]
FROM [Tabela de Prescrições]
ORDER BY [Tabela de Prescrições].[Título da Prescrição];

SELECT DISTINCTROW pacientes.*
FROM pacientes
WHERE (((pacientes.ID)=RetFiltro_IDPaciente()))
WITH OWNERACCESS OPTION;

SELECT DISTINCTROW História.*
FROM História
WHERE (((História.ID)=RetFiltro_IDPaciente()))
ORDER BY História.[Data do Exame]
WITH OWNERACCESS OPTION;

SELECT DISTINCTROW Obstétrico.*, pacientes.Rubéola, pacientes.GS, pacientes.RH, pacientes.Gesta, pacientes.Para, Calc_Idade([Nasc]) AS Idade, [Nome] & " " & [Sobrenome] AS PNome
FROM pacientes INNER JOIN Obstétrico ON pacientes.ID = Obstétrico.[ID da Paciente]
WHERE (((Obstétrico.[ID da Paciente])=RetFiltro_IDPaciente()))
WITH OWNERACCESS OPTION;

SELECT DISTINCTROW [Exames Obstétricos].*, Obstétrico.DUM
FROM Obstétrico INNER JOIN [Exames Obstétricos] ON Obstétrico.ID = [Exames Obstétricos].[ID do Obstétrico]
ORDER BY [Exames Obstétricos].Data
WITH OWNERACCESS OPTION;

SELECT [Nome] & " " & [Sobrenome] AS NomePaciente, pacientes.ID
FROM pacientes;

SELECT DISTINCTROW Procedimentos.*
FROM Procedimentos
WHERE (((Procedimentos.[ID da Paciente])=RetFiltro_IDPaciente()))
ORDER BY Procedimentos.Data
WITH OWNERACCESS OPTION;

SELECT DISTINCTROW Obstétrico.*, [Exames Obstétricos].*, pacientes.Rubéola, pacientes.GS, pacientes.RH, pacientes.Gesta, pacientes.Para, Calc_Idade([Nasc]) AS Idade, [Nome] & " " & [Sobrenome] AS PNome, Obstétrico.ID AS Flt_IDObst
FROM pacientes INNER JOIN (Obstétrico INNER JOIN [Exames Obstétricos] ON Obstétrico.ID = [Exames Obstétricos].[ID do Obstétrico]) ON pacientes.ID = Obstétrico.[ID da Paciente]
WITH OWNERACCESS OPTION;