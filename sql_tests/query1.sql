SELECT a."REG_ANS", a.despesa, b."Razao_Social", b."CNPJ"
FROM (
	SELECT dc."REG_ANS", SUM(dc."VL_SALDO_INICIAL" - dc."VL_SALDO_FINAL") AS despesa FROM demons_cont dc
	WHERE
	dc."DESCRICAO" = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR ' AND 
	dc."DATA" BETWEEN '2022-10-01' AND '2022-12-31'
	GROUP BY dc."REG_ANS"
	) AS a
LEFT JOIN (
	SELECT op."Registro_ANS", op."Razao_Social", op."CNPJ" 
	FROM operadoras op
) AS b
ON a."REG_ANS" = b."Registro_ANS"
ORDER BY a.despesa DESC
LIMIT 10;



-- Apos o banco estar configurado e com os dados, foi feita a query acima no DBeaver, obtendo o resultado abaixo.
---------------------------------------------------------------------------------------------------------------------
------------------------------------------------ RETORNO DA QUERY ---------------------------------------------------
---------------------------------------------------------------------------------------------------------------------
-- REG_ANS	  despesa	            Razao_Social	                                                CNPJ           --
---------------------------------------------------------------------------------------------------------------------
-- 422631	  141,906,915.1	        ASSOCIAÇÃO PETROBRAS DE SAÚDE - APS	                            39427632000171 --
-- 325082	  983,421.5199999989	UNIMED DO OESTE DA BAHIA COOPERATIVA DE TRABALHO MÉDICO	        34063123000193 --
-- 414689	  500,435.8800000001	FUNDO DE ASSISTÊNCIA À SAÚDE DOS FUNCIONÁRIOS DO BEC	        04839091000104 --
-- 349194	  410,064.4000000001	 	                                                                           --
-- 407011	  247,258.32	        GAMA SAUDE LTDA.	                                            02009924000184 --
-- 311057	  86,300.43	            UNIMED VALE DO URUCUIA - COOPERATIVA DE TRABALHO MEDICO LTDA	01371135000126 --
-- 422053	  57,059.31	            ASSOCIAÇÃO FCA SAÚDE	                                        33922160000147 --
-- 350362	  4,464.82	 	                                                                                       --
-- 418285	  330	                FUNDAÇÃO FIAT SAÚDE E BEM ESTAR	                                12838821000180 --
-- 305995	  0	                    GOOD LIFE SAUDE LTDA	                                        65140725000120 --
---------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------
