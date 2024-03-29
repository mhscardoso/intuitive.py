select a."REG_ANS", a.despesa, b."Razao_Social", b."CNPJ"
from (
	select dc."REG_ANS", SUM(dc."VL_SALDO_INICIAL" - dc."VL_SALDO_FINAL") as despesa from demons_cont dc
	where
	dc."DESCRICAO" = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR ' and 
	dc."DATA" BETWEEN '2023-01-01' and '2023-12-31'
	group by dc."REG_ANS"
	) as a
left join (
	select op."Registro_ANS", op."Razao_Social", op."CNPJ" from operadoras op
) as b
on a."REG_ANS" = b."Registro_ANS"
order by a.despesa desc
limit 10;


-- Apos o banco estar configurado e com os dados, foi feita a query acima no DBeaver, obtendo o resultado abaixo.
--------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------- RETORNO DA QUERY -------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------------
-- REG_ANS	   despesa	      Razao_Social	                                                                   CNPJ           --
--------------------------------------------------------------------------------------------------------------------------------
-- 418072	   3,243,687.43	  CAIXA SEGURADORA ESPECIALIZADA EM SAÚDE S/A	                                   13223975000120 --
-- 311057	   305,340.47	  UNIMED VALE DO URUCUIA - COOPERATIVA DE TRABALHO MEDICO LTDA	                   01371135000126 --
-- 333689	   0	          MEDISERVICE OPERADORA DE PLANOS DE SAÚDE S.A.	                                   57746455000178 --
-- 393533	   0	          ASSOCIAÇÃO DO FISCO DE ALAGOAS	                                               12317012000123 --
-- 322890	   0	          DENTALPAR ASSISTÊNCIA ODONTOLÓGICA EMPRESARIAL LTDA.	                           02156150000114 --
-- 314366	   0	          DENTAL PLUS CONVÊNIO ODONTOLÓGICO LTDA.	                                       00571628000147 --
-- 334511	   0	          UNIMED VALE DO PARAÍBA - FEDERAÇÃO INTRAFEDERATIVA DAS COOPERATIVAS MÉDICAS	   01773319000112 --
-- 339636	   0	          FUNDAÇÃO DE ASSISTÊNCIA E PREVIDÊNCIA SOCIAL DO BNDES                        	   00397695000197 --
-- 310131	   0	          UNIMED PLANALTO - COOPERATIVA DE TRABALHO MÉDICO	                               36862415000111 --
-- 413283	   0	          AESP ODONTO ASSISTÊNCIA ODONTOLÓGICA S/S LTDA EPP	                               03694367000140 --
--------------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------------
