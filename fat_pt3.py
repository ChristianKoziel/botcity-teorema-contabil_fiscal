from botcity.core import DesktopBot
from botcity.maestro import *

BotMaestroSDK.RAISE_NOT_CONNECTED = False

maestro = BotMaestroSDK.from_sys_args()
execution = maestro.get_execution()





"""
CÓDIGO FEITO PARA SISTEMA FATURAMENTO 24.11 PARTE 2 
O CÓDIGO FOI FEITO UTILIZANDO A RESOLUÇÃO 1366 x 768 com TAMANHO DE TEXTO 100%
O SISTEMA TAMBÉM DEVE ESTAR EM TELA CHEIA PARA QUE FUNCIONE CORRETAMENTE
BASE - ICTUS 0000024
"""

class Bot(DesktopBot) :


    def find_button(self, label) :
        try :
            if not self.find(label,  matching=0.97, waiting_time=10000) :
                raise Exception("Element not found")
        except Exception as error :
            print("Error")
            filepath = self.save_screenshot(r"C:\Users\Usuário\Desktop\printserros\screenshot.png")
            maestro.error(task_id=execution.task_id,
                          exception=error,
                          screenshot=filepath)
            maestro.alert(task_id=execution.task_id,
                          title="Title",
                          message="Erro ao executar o Bot",
                          alert_type=AlertType.ERROR)




    def action(self,execution=None) :
                bot = self
                """
                # COMPRAS 
 
                ###################################################################
                
                
                self.wait(1500)
                if not bot.find( "fatu_btn_compras_menu_1", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_compras_menu_1")
                bot.click()
                self.wait(1500)
                self.type_down()
                self.wait(1500)
                if not self.find( "requisicoesdecompra", matching=0.97, waiting_time=10000):
                    self.not_found("requisicoesdecompra")
                self.click()
                if not bot.find( "fatu_compras_central_rel_data", matching=0.97, waiting_time=10000):
                    not_found("fatu_compras_central_rel_data")
                bot.click_relative(314, 110)
                if not self.find( "carregaranoreqcompras", matching=0.97, waiting_time=10000):
                    self.not_found("carregaranoreqcompras")
                self.click()
                if not self.find( "anoanteriorreqcompras", matching=0.97, waiting_time=10000):
                    self.not_found("anoanteriorreqcompras")
                self.click()            
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                self.tab()
                x=0
                while x<5:
                    self.type_down()
                    x=x+1
                self.tab()
                self.space()
                x=0
                while x<7:
                    self.space()
                    self.type_down()
                    x=x+1  
                self.space()          
                x=0
                while x<7:
                    self.space()
                    self.type_up()
                    x=x+1          
                self.tab()
                if not self.find( "usuariosolicitante", matching=0.97, waiting_time=10000):
                    self.not_found("usuariosolicitante")
                self.click_relative(45, 25)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                self.tab()
                if not self.find( "usuarioautorizador", matching=0.97, waiting_time=10000):
                    self.not_found("usuarioautorizador")
                self.click_relative(42, 23)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                self.tab()
                if not self.find( "reqcompraautorizado", matching=0.97, waiting_time=10000):
                    self.not_found("reqcompraautorizado")
                self.click()
                if not self.find( "reqcompranautorizado", matching=0.97, waiting_time=10000):
                    self.not_found("reqcompranautorizado")
                self.click()
                if not self.find( "reqcomprapendentes", matching=0.97, waiting_time=10000):
                    self.not_found("reqcomprapendentes")
                self.click()
                if not self.find( "reqcomprascotando", matching=0.97, waiting_time=10000):
                    self.not_found("reqcomprascotando")
                self.click()
                if not self.find( "reqcomprastodos", matching=0.97, waiting_time=10000):
                    self.not_found("reqcomprastodos")
                self.click()
                
                                ####---SELEÇÃO ABA1---####
                                
                if not self.find( "abaselecao", matching=0.97, waiting_time=10000):
                    self.not_found("abaselecao")
                self.click()
                if not self.find( "transacao", matching=0.97, waiting_time=10000):
                    self.not_found("transacao")
                self.click_relative(10, 42)
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.space()
                self.space()
                self.tab()
                self.space()
                self.space()
                if not self.find( "buscarclassificacaoCC", matching=0.97, waiting_time=10000):
                    self.not_found("buscarclassificacaoCC")
                self.click_relative(64, 40)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                if not self.find( "buscarcentrodecustosCC", matching=0.97, waiting_time=10000):
                    self.not_found("buscarcentrodecustosCC")
                self.click_relative(85, 82)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                if not self.find( "buscarservicoCC", matching=0.97, waiting_time=10000):
                    self.not_found("buscarservicoCC")
                self.click_relative(62, 123)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.enter()
                self.backspace()
                if not self.find( "buscarcompradorCC", matching=0.97, waiting_time=10000):
                    self.not_found("buscarcompradorCC")
                self.click_relative(464, 43)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                if not self.find( "buscarcentrodecustosservicoCC", matching=0.97, waiting_time=10000):
                    self.not_found("buscarcentrodecustosservicoCC")
                self.click_relative(486, 85)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                if not self.find( "buscarcondicaopagCC", matching=0.97, waiting_time=10000):
                    self.not_found("buscarcondicaopagCC")
                self.click_relative(865, 40)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                if not self.find( "buscaritemCC", matching=0.97, waiting_time=10000):
                    self.not_found("buscaritemCC")
                self.click_relative(867, 85)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                
                
                
                
                                ####---ABA1 REQCOMPRAS---####
                
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                self.tab()
                #if not self.find( "solicitantereqcompras", matching=0.97, waiting_time=10000):
                #    self.not_found("solicitantereqcompras")           
                #self.click_relative(54, 25)
                if not bot.find( "fatu_compras_movimento_requisicoes_rel_solicitante", matching=0.97, waiting_time=10000):
                    not_found("fatu_compras_movimento_requisicoes_rel_solicitante")
                bot.click_relative(439, 155)                      
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                self.tab()
                if not self.find( "solicitantereqcompras", matching=0.97, waiting_time=10000):
                    self.not_found("solicitantereqcompras")
                self.click_relative(54, 25)
                self.tab()
                self.tab()
                self.tab()
                x=0
                while x<30:
                    self.type_down()
                    x=x+1
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.tab()
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                
                                ####---ABA2 REQCOMPRAS---####
                
                if not self.find( "aba2reqcompras", matching=0.97, waiting_time=10000):
                    self.not_found("aba2reqcompras")
                self.click()
                if not self.find( "addregistroaba2reqcompras", matching=0.97, waiting_time=10000):
                    self.not_found("addregistroaba2reqcompras")
                self.click()            
                if not self.find( "buscaritensreqcompras", matching=0.97, waiting_time=10000):
                    self.not_found("buscaritensreqcompras")
                self.click_relative(10, 31)
                self.type_keys_with_interval(1,'agulha gengival')
                self.enter()
                self.type_down()
                self.type_down()
                self.type_down()
                self.type_down()
                self.wait(500)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # self.wait(500)
                # if not self.find( "quantidade_lancitens", matching=0.97, waiting_time=10000):
                #     self.not_found("quantidade_lancitens")
                # self.click_relative(336, 280)
                # self.backspace()
                # self.enter()
                # x=0
                # while x<31:
                #     self.type_down()
                #     x=x+1
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # self.wait(500)
                
                self.type_keys_with_interval(1,'1')
                self.tab()
                self.tab()
                self.tab()
                self.tab()
                self.type_down()
                if not self.find( "botaoconfirmaritensreqcompras", matching=0.97, waiting_time=10000):
                    self.not_found("botaoconfirmaritensreqcompras")
                self.click()
                self.wait(3000)
 
                #if not bot.find( "fatu_compras_avisos_retornar_itens", matching=0.97, waiting_time=10000):
                #    not_found("fatu_compras_avisos_retornar_itens")
                #bot.click()
                #self.wait(2000)
                
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
               
                
                                ####---ABA3 REQCOMPRAS---####
                                
                if not self.find( "aba3servicosreqcompras", matching=0.97, waiting_time=10000):
                    self.not_found("aba3servicosreqcompras")
                self.click()
                if not self.find( "addregistroaba2reqcompras", matching=0.97, waiting_time=10000):
                    self.not_found("addregistroaba2reqcompras")
                self.click()
                if not self.find( "buscarservicoaba3reqcompras", matching=0.97, waiting_time=10000):
                    self.not_found("buscarservicoaba3reqcompras")
                self.click_relative(62, 24)
                self.backspace()
                self.enter()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.enter()
                self.tab()
                self.tab()
                self.type_down()
                if not self.find( "buscarclassificacaoaba3reqcompras", matching=0.97, waiting_time=10000):
                    self.not_found("buscarclassificacaoaba3reqcompras")
                self.click_relative(54, 22)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "buscarcentrodecustosreqcompras", matching=0.97, waiting_time=10000):
                    self.not_found("buscarcentrodecustosreqcompras")
                self.click_relative(79, 24)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "obsaba3reqcompras", matching=0.97, waiting_time=10000):
                    self.not_found("obsaba3reqcompras")
                self.click_relative(9, 20)
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "gravarregistroaba3", matching=0.97, waiting_time=10000):
                    self.not_found("gravarregistroaba3")
                self.click()
                if not self.find( "cancelarregistroaba3", matching=0.97, waiting_time=10000):
                    self.not_found("cancelarregistroaba3")
                self.click()
                
                                ####---ABA4 REQCOMPRAS---####
                                
                if not self.find( "aba4reqcompras", matching=0.97, waiting_time=10000):
                    self.not_found("aba4reqcompras")
                self.click()
                if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                    self.not_found("salvarrs")
                self.click()
                
                                ####---BOTÕES NAS ABAS---####
                                
                if not self.find( "processos", matching=0.97, waiting_time=10000):
                    self.not_found("processos")
                self.click_relative(74, -4)
                if not self.find( "anexardocumentos2", matching=0.97, waiting_time=10000):
                    self.not_found("anexardocumentos2")
                self.click()
                
                if not bot.find( "fatu_compras_anexo_de_arquivo_add", matching=0.97, waiting_time=10000):
                    not_found("fatu_compras_anexo_de_arquivo_add")
                bot.click_relative(-16, 71)
                if not self.find( "abrirselecaodearquivos", matching=0.97, waiting_time=10000):
                    self.not_found("abrirselecaodearquivos")
                self.click()
                #if not self.find( "cancelaranexo", matching=0.97, waiting_time=10000):
                #    self.not_found("cancelaranexo")
                #self.click_relative(599, 418)
                self.key_esc()
                if not self.find( "cancelaranexodearquivos", matching=0.97, waiting_time=10000):
                    self.not_found("cancelaranexodearquivos")
                self.click()
                self.key_esc()
                #if not self.find( "retornaranexoarquivos", matching=0.97, waiting_time=10000):
                #    self.not_found("retornaranexoarquivos")
                #self.click_relative(23, 44)
                if not self.find( "email", matching=0.97, waiting_time=10000):
                    self.not_found("email")
                self.click_relative(64, -3)
                if not self.find( "enviaremail", matching=0.97, waiting_time=10000):
                    self.not_found("enviaremail")
                self.click()
                if not bot.find( "fatu_compras_btn_retornar_email", matching=0.97, waiting_time=10000):
                    not_found("fatu_compras_btn_retornar_email")
                bot.click_relative(14, 37)
                self.wait(1000)
                self.enter()
                if not self.find( "email", matching=0.97, waiting_time=10000):
                    self.not_found("email")
                self.click_relative(64, -3)
                if not self.find( "editarpdfemail", matching=0.97, waiting_time=10000):
                    self.not_found("editarpdfemail")
                self.click()
                self.wait(3000)
                if not bot.find( "fatu_compras_btn_fechar_relatorios_rel", matching=0.97, waiting_time=10000):
                    not_found("fatu_compras_btn_fechar_relatorios_rel")
                bot.click_relative(1237, 3)
                self.wait(2000)
                if not bot.find( "fatu_data_tree_relativo_fechar", matching=0.97, waiting_time=10000):
                    not_found("fatu_data_tree_relativo_fechar")
                bot.click_relative(155, -128)
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()
                #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                #    self.not_found("simexcluirrs")
                #self.click()
                self.enter()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                                ####---COTACOES DE COMPRA---####
                                
                if not self.find( "cotacoesdecompras", matching=0.97, waiting_time=10000):
                    self.not_found("cotacoesdecompras")
                self.click()          
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()            
                self.enter()
                if not bot.find( "fatu_compras_origem_periodo_rel", matching=0.97, waiting_time=10000):
                    not_found("fatu_compras_origem_periodo_rel")
                bot.click_relative(104, 24)
                self.wait(500)
                self.click()
                x=0
                while x<5:
                    self.type_down()
                    x=x+1
                self.tab()
                self.space()
                x=0
                while x<7:
                    self.space()
                    self.type_down()
                    x=x+1  
                self.space()          
                x=0
                while x<7:
                    self.space()
                    self.type_up()
                    x=x+1          
                self.tab()
                if not self.find( "usuariosolicitante", matching=0.97, waiting_time=10000):
                    self.not_found("usuariosolicitante")
                self.click_relative(45, 25)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                self.tab()
                if not self.find( "usuarioautorizador", matching=0.97, waiting_time=10000):
                    self.not_found("usuarioautorizador")
                self.click_relative(42, 23)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                self.tab()
                if not self.find( "buscarclientefornecedor", matching=0.97, waiting_time=10000):
                    self.not_found("buscarclientefornecedor")
                self.click_relative(75, 24)
                self.enter()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                self.tab()
                
                                ####---SELECAO COTACAO---####
                                
                if not self.find( "abaselecao", matching=0.97, waiting_time=10000):
                    self.not_found("abaselecao")
                self.click()
                if not self.find( "transacao", matching=0.97, waiting_time=10000):
                    self.not_found("transacao")
                self.double_click_relative(10, 42)
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.space()
                self.space()
                self.tab()
                self.space()
                self.space()
                if not self.find( "buscarclassificacaoCC", matching=0.97, waiting_time=10000):
                    self.not_found("buscarclassificacaoCC")
                self.click_relative(64, 40)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                if not self.find( "buscarcentrodecustosCC", matching=0.97, waiting_time=10000):
                    self.not_found("buscarcentrodecustosCC")
                self.click_relative(85, 82)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                if not self.find( "buscarservicoCC", matching=0.97, waiting_time=10000):
                    self.not_found("buscarservicoCC")
                self.click_relative(62, 123)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.enter()
                self.backspace()
                if not self.find( "buscarcompradorCC", matching=0.97, waiting_time=10000):
                    self.not_found("buscarcompradorCC")
                self.click_relative(464, 43)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                if not self.find( "buscarcentrodecustosservicoCC", matching=0.97, waiting_time=10000):
                    self.not_found("buscarcentrodecustosservicoCC")
                self.click_relative(486, 85)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                if not self.find( "buscarcondicaopagCC", matching=0.97, waiting_time=10000):
                    self.not_found("buscarcondicaopagCC")
                self.click_relative(865, 40)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                if not self.find( "buscaritemCC", matching=0.97, waiting_time=10000):
                    self.not_found("buscaritemCC")
                self.click_relative(867, 85)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                
                                ####---PEDIDOS DE COMPRA---####
                                
                if not bot.find( "fatu_compras_btn_3_pedidos_", matching=0.97, waiting_time=10000):
                    not_found("fatu_compras_btn_3_pedidos_")
                bot.click()                                                    
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                self.enter()
                if not bot.find( "fatu_compras_3_pedidos_rel_origem", matching=0.97, waiting_time=10000):
                    not_found("fatu_compras_3_pedidos_rel_origem")
                bot.click_relative(299, 47)
                self.wait(1500)
                self.click()
                self.tab()
                x=0
                while x<5:
                    self.type_down()
                    x=x+1
                self.tab()
                self.space()
                x=0
                while x<6:
                    self.space()
                    self.type_down()
                    x=x+1  
                self.space()          
                x=0
                while x<6:
                    self.space()
                    self.type_up()
                    x=x+1          
                self.tab()
                if not self.find( "usuariosolicitante", matching=0.97, waiting_time=10000):
                    self.not_found("usuariosolicitante")
                self.click_relative(45, 25)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                self.tab()
                if not self.find( "usuarioautorizador", matching=0.97, waiting_time=10000):
                    self.not_found("usuarioautorizador")
                self.click_relative(42, 23)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                self.tab()
                if not self.find( "buscarclientefornecedor", matching=0.97, waiting_time=10000):
                    self.not_found("buscarclientefornecedor")
                self.click_relative(75, 24)
                self.enter()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                self.tab()
                
                                ####---SELEÇÃO PEDIDOS COMPRA---####
                
                # if not self.find( "abaselecao", matching=0.97, waiting_time=10000):
                #     self.not_found("abaselecao")
                # self.click()
                # if not self.find( "transacao", matching=0.97, waiting_time=10000):
                #     self.not_found("transacao")
                # self.click_relative(10, 42)
                # self.type_keys_with_interval(1,'te12!@')
                # #if not self.find( "selecaoparcialpedidos", matching=0.97, waiting_time=10000):
                # #    self.not_found("selecaoparcialpedidos")
                # #self.click()
                # #if not self.find( "selecaonenhumpedidos", matching=0.97, waiting_time=10000):
                # #    self.not_found("selecaonenhumpedidos")
                # #self.click()
                # #if not self.find( "selecaotodospedidos", matching=0.97, waiting_time=10000):
                # #    self.not_found("selecaotodospedidos")
                # #self.click_relative(7, 25)            
                # self.tab()
                # self.space()
                # self.space()
                # self.tab()
                # self.space()
                # self.space()
                # #codigo de operacao
                # if not self.find( "buscarclassificacaoCC", matching=0.97, waiting_time=10000):
                #     self.not_found("buscarclassificacaoCC")
                # self.click_relative(64, 40)
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # self.wait(500)
                # self.backspace()
                # #condicao de pagamento
                # if not self.find( "condicaodepagamentopedidos", matching=0.97, waiting_time=10000):
                #     self.not_found("condicaodepagamentopedidos")
                # self.click_relative(61, 83)
                
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # self.wait(500)
                # self.backspace()
                # #centro de custos serviços
                # if not self.find( "centrodecustospedidos", matching=0.97, waiting_time=10000):
                #     self.not_found("centrodecustospedidos")
                # self.click_relative(85, 125)            
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # self.wait(500)
                # self.backspace()
                # #classificacao
                # if not self.find( "buscarcompradorCC", matching=0.97, waiting_time=10000):
                #     self.not_found("buscarcompradorCC")
                # self.click_relative(464, 43)
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # self.wait(500)
                # self.backspace()
                # #transportador
                # if not self.find( "buscartransportadorpedidos", matching=0.97, waiting_time=10000):
                #     self.not_found("buscartransportadorpedidos")
                # self.click_relative(464, 82)
                # self.enter() 
                # self.type_down()
                # self.type_down()           
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # self.wait(500)
                # self.backspace()
                # #comprador
                # if not self.find( "buscarcondicaopagCC", matching=0.97, waiting_time=10000):
                #     self.not_found("buscarcondicaopagCC")
                # self.click_relative(865, 40)
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # self.wait(500)
                # self.backspace()
                # #centro de custos
                # if not self.find( "buscarcentrodecustospedidoscompras", matching=0.97, waiting_time=10000):
                #     self.not_found("buscarcentrodecustospedidoscompras")
                # self.click_relative(886, 84)
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # self.wait(500)
                # self.backspace()
                # #item
                # if not self.find( "buscaritempedidos", matching=0.97, waiting_time=10000):
                #     self.not_found("buscaritempedidos")
                # self.click_relative(464, 122)
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # self.wait(500)
                # self.backspace()
                # #servico
                # if not self.find( "buscarservicopedidos", matching=0.97, waiting_time=10000):
                #     self.not_found("buscarservicopedidos")
                # self.click_relative(864, 124)
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # self.wait(500)
                # self.enter()
                # self.backspace()
                
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                                ####---PRÉ COMPRA---####
                                
                # self.wait(1500)
                # if not bot.find( "fatu_btn_compras_menu_1", matching=0.97, waiting_time=10000):
                #     not_found("fatu_btn_compras_menu_1")
                # bot.click()
                # #self.type_down()
                # self.wait(1500)
                # if not self.find( "precompra", matching=0.97, waiting_time=10000):
                #     self.not_found("precompra")
                # self.click()
                # if not self.find( "2selecao", matching=0.97, waiting_time=10000):
                #     self.not_found("2selecao")
                # self.click()
                # if not self.find( "abaitens", matching=0.97, waiting_time=10000):
                #     self.not_found("abaitens")
                # self.click()            
                # if not self.find( "filtro", matching=0.97, waiting_time=10000):
                #     self.not_found("filtro")
                # self.click()
                # if not self.find( "retornarfiltragem", matching=0.97, waiting_time=10000):
                #     self.not_found("retornarfiltragem")
                # self.click_relative(39, 51)
                # if not self.find( "addregistroprecompra", matching=0.97, waiting_time=10000):
                #     self.not_found("addregistroprecompra")
                # self.click()
                # if not self.find( "buscaritensreqcompras", matching=0.97, waiting_time=10000):
                #     self.not_found("buscaritensreqcompras")
                # self.click_relative(10, 31)
                # self.type_keys_with_interval(1,'agulha gengival')
                # self.enter()
                # self.type_down()
                # self.type_down()
                # self.type_down()
                # self.type_down()
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # self.wait(1500)
                # if not self.find( "botaoconfirmaritensreqcompras", matching=0.97, waiting_time=10000):
                #     self.not_found("botaoconfirmaritensreqcompras")
                # self.click()
                # self.wait(3000)
                # if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                #     self.not_found("retornarfim")
                # self.click()
                # #if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                # #    self.not_found("selecionarmunicipiovcr")
                # #self.click()
                # #if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                # #    self.not_found("retornarpe")
                # #self.click()
                # if not self.find( "abcdemanda", matching=0.97, waiting_time=10000):
                #     self.not_found("abcdemanda")
                # self.click()
                # if not self.find( "retornargeracaocurvas", matching=0.97, waiting_time=10000):
                #     self.not_found("retornargeracaocurvas")
                # self.click_relative(32, 45)
                # if not self.find( "geracao", matching=0.97, waiting_time=10000):
                #     self.not_found("geracao")
                # self.click_relative(63, -2)
                # 
                # if not self.find( "requisicaodecompras", matching=0.97, waiting_time=10000):
                #     self.not_found("requisicaodecompras")
                # self.click()
                # self.enter()
                # if not self.find( "geracao", matching=0.97, waiting_time=10000):
                #     self.not_found("geracao")
                # self.click_relative(63, -2)
                # if not self.find( "cotacaodecompra", matching=0.97, waiting_time=10000):
                #     self.not_found("cotacaodecompra")
                # self.click()
                # self.enter()
                # if not self.find( "geracao", matching=0.97, waiting_time=10000):
                #     self.not_found("geracao")
                # self.click_relative(63, -2)
                
                # if not self.find( "gerarpedidodecompraprecompra", matching=0.97, waiting_time=10000):
                #     self.not_found("gerarpedidodecompraprecompra")
                # self.click()
                # if not self.find( "buscarfornecedorgp", matching=0.97, waiting_time=10000):
                #     self.not_found("buscarfornecedorgp")
                # self.click_relative(196, 40)
                # self.wait(1000)
                # self.type_keys_with_interval(1,'0081260')
                # self.enter()
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # self.wait(500)
                # if not self.find( "buscaroperacao", matching=0.97, waiting_time=10000):
                #     self.not_found("buscaroperacao")
                # self.click_relative(65, 240)
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # self.wait(500)
                # if not self.find( "buscarcondicaodepagamentogp", matching=0.97, waiting_time=10000):
                #     self.not_found("buscarcondicaodepagamentogp")
                # self.click_relative(65, 272)
                # if not self.find( "buscarcompradorgp", matching=0.97, waiting_time=10000):
                #     self.not_found("buscarcompradorgp")
                # self.click_relative(488, 241)
                # if not self.find( "cancelarfornecedorgeracaodopedido", matching=0.97, waiting_time=10000):
                #     self.not_found("cancelarfornecedorgeracaodopedido")
                # self.click()
                # self.enter()
                # 
                # if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                #     self.not_found("retornarfim")
                # self.click()
                
                                ####---CONSULTA STATUS SOLICITACAO---####
                self.wait(1500)

                if not bot.find( "fatu_btn_compras_menu_1", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_compras_menu_1")
                bot.click()
                if not self.find( "consultastatussolicitacao", matching=0.97, waiting_time=10000):
                    self.not_found("consultastatussolicitacao")
                self.click()
                if not bot.find( "fatu_compras_solicitacao_item", matching=0.97, waiting_time=10000):
                    not_found("fatu_compras_solicitacao_item")
                bot.click_relative(57, 36)
                self.type_keys_with_interval(1,'123')
                self.enter()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "solicitanteCSM", matching=0.97, waiting_time=10000):
                    self.not_found("solicitanteCSM")
                self.click_relative(184, 31)
                self.enter()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                                ####---ACORDO COMERCIAL---####
                                
                # if not bot.find( "fatu_btn_compras_menu_1", matching=0.97, waiting_time=10000):
                #     not_found("fatu_btn_compras_menu_1")
                # bot.click()
                # if not self.find( "acordocomercial", matching=0.97, waiting_time=10000):
                #     self.not_found("acordocomercial")
                # self.click()
                # if not self.find( "acordocomercial2", matching=0.97, waiting_time=10000):
                #     self.not_found("acordocomercial2")
                # self.click()
                # self.backspace()
                # self.enter()
                # if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                #     not_found("fatu_btn_incluir_opc_1_2411")
                # bot.click()
                # if not self.find( "buscarfornecedorCAcordos", matching=0.97, waiting_time=10000):
                #     self.not_found("buscarfornecedorCAcordos")
                # self.click_relative(131, 6)
                # if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                #     self.not_found("localizarfim")
                # self.click()
                # self.wait(2000)
                # x=0
                # while x<18:
                #     self.type_down()
                #     x=x+1
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # self.wait(500)
                # self.tab()
                # self.tab()
                # self.type_keys_with_interval(1,'123')
                # self.tab()
                # self.type_keys_with_interval(1,'123')
                # self.tab()
                # x=0
                # while x<3:
                #     self.type_down()
                #     x=x+1
                # self.tab()
                # self.type_keys_with_interval(1,'123')
                # self.tab()
                # self.type_keys_with_interval(1,'te12!@')
                # self.tab()
                # if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                #     self.not_found("salvarrs")
                # self.click()
                # if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                #     self.not_found("retornarfim")
                # self.click()
                # if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                #     self.not_found("localizarfim")
                # self.click()
                # if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                #     self.not_found("editarfim")
                # self.click()
                # if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                #     self.not_found("excluirrs")
                # self.click()
                # #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                # #    self.not_found("simexcluirrs")
                # #self.click()
                # self.enter()
                # if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                #     self.not_found("retornarfim")
                # self.click()
                # if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                #     self.not_found("retornarfim")
                # self.click()
                
                                ####---CONTA CORRENTE FORNECEDORES---####
                                
                # if not bot.find( "fatu_btn_compras_menu_1", matching=0.97, waiting_time=10000):
                #     not_found("fatu_btn_compras_menu_1")
                # bot.click()
                # if not self.find( "acordocomercial", matching=0.97, waiting_time=10000):
                #     self.not_found("acordocomercial")
                # self.click()
                # if not self.find( "contacorrendefornecedores", matching=0.97, waiting_time=10000):
                #     self.not_found("contacorrendefornecedores")
                # self.click()
                # self.enter()            
                # if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                #     not_found("fatu_btn_incluir_opc_1_2411")
                # bot.click()
                # self.enter()
                # if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                #     self.not_found("retornarfim")
                # self.click()
                # self.key_esc()
                """
                ######################################################
                ######################################################
                ####################---VENDAS---######################
                ######################################################

                

                self.wait(1500)
                if not bot.find( "fatu_btn_menu_vendas_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_menu_vendas_2411")
                bot.click()
                
                #self.type_down()
                self.wait(1500)
                if not self.find( "orcamentos", matching=0.97, waiting_time=10000):
                    self.not_found("orcamentos")
                self.click()        
                self.wait(1500)
                self.enter()
                if not bot.find( "fatu_vendas_btn_cliente_2_orc", matching=0.97, waiting_time=10000):
                    not_found("fatu_vendas_btn_cliente_2_orc")
                bot.click()
                if not bot.find( "fatu_vendas_btn_cliente_busc", matching=0.97, waiting_time=10000):
                    not_found("fatu_vendas_btn_cliente_busc")
                bot.click()
                self.wait(2000)
                self.type_keys_with_interval(1,'0081260')
                self.enter()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                self.tab()
                if not bot.find( "fatu_vendas_btn_sistema_origem", matching=0.97, waiting_time=10000):
                    not_found("fatu_vendas_btn_sistema_origem")
                bot.click()
                x=0
                while x<15:
                    self.type_down()
                    x=x+1
                x=0
                while x<15:
                    self.type_up()
                    x=x+1
                self.tab()
                x=0
                while x<6:
                    self.type_down()
                    x=x+1
                x=0
                while x<6:
                    self.type_up()
                    x=x+1
                self.tab()
                self.space()
                x=0
                while x<12:
                    self.type_down()
                    self.space()
                    x=x+1
                self.space()
                x=0
                while x<12:
                    self.type_up()
                    self.space()
                    x=x+1
                if not bot.find( "fatu_btn_vendas_selecao_mv", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_vendas_selecao_mv")
                bot.click()
                if not self.find( "transacaoselecaoMV", matching=0.97, waiting_time=10000):
                    self.not_found("transacaoselecaoMV")
                self.click_relative(7, 44)
                self.type_keys_with_interval(1,'t1!')
                self.backspace()
                self.backspace()
                self.backspace()
                self.tab()
                x=0
                while x<5:
                    self.type_keys_with_interval(1,'874')
                    self.backspace()
                    self.backspace()
                    self.backspace()
                    self.tab()
                    x=x+1
                self.space()
                self.space()
                self.tab()
                x=0
                while x<4:
                    self.type_keys_with_interval(1,'874')
                    self.backspace()
                    self.backspace()
                    self.backspace()
                    self.tab()
                    x=x+1
                x=0
                while x<3:
                    self.type_keys_with_interval(1,'te12@!')
                    self.backspace()
                    self.backspace()
                    self.backspace()
                    self.backspace()
                    self.backspace()
                    self.backspace()
                    self.tab()
                    x=x+1
                if not self.find( "buscarclassMV", matching=0.97, waiting_time=10000):
                    self.not_found("buscarclassMV")
                self.click_relative(63, 42)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                if not self.find( "buscarrotaMV", matching=0.97, waiting_time=10000):
                    self.not_found("buscarrotaMV")
                self.click_relative(65, 83)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                if not self.find( "buscarvendedorMV", matching=0.97, waiting_time=10000):
                    self.not_found("buscarvendedorMV")
                self.click_relative(464, 41)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                if not self.find( "buscaritemMV", matching=0.97, waiting_time=10000):
                    self.not_found("buscaritemMV")
                self.click_relative(463, 188)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                if not self.find( "buscarcondicaodepagamentoMV", matching=0.97, waiting_time=10000):
                    self.not_found("buscarcondicaodepagamentoMV")
                self.click_relative(865, 44)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                if not self.find( "selecionarstatusMV", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarstatusMV")
                self.click_relative(1178, 78)
                self.type_down()
                self.enter()
                self.wait(500)
                if not self.find( "selecionarstatusMV", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarstatusMV")
                self.click_relative(1178, 78)
                self.backspace()
                if not self.find( "selecao2orcamentos", matching=0.97, waiting_time=10000):
                    self.not_found("selecao2orcamentos")
                self.click()
                if not self.find( "buscartransportadorMV", matching=0.97, waiting_time=10000):
                    self.not_found("buscartransportadorMV")
                self.click_relative(63, 83)
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                self.wait(2500)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "selecionartransportadorMV", matching=0.97, waiting_time=10000):
                    self.not_found("selecionartransportadorMV")
                self.double_click_relative(42, 83)           
                self.backspace()
                
                                ####---INCLUIR ORCAMENTO---####
                                
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                if not self.find( "b_codigoop_Orc", matching=0.97, waiting_time=10000):
                    self.not_found("b_codigoop_Orc")
                self.click_relative(70, 184)
                if not self.find( "CONFIGCLIENTES_aba2", matching=0.97, waiting_time=10000):
                    self.not_found("CONFIGCLIENTES_aba2")
                self.click()
                if not self.find( "op_todas_manutencao_botaoteste", matching=0.97, waiting_time=10000):
                    self.not_found("op_todas_manutencao_botaoteste")
                self.click_relative(9, 30)
                self.enter()
                self.enter()
                self.enter()           
                self.backspace()
                self.enter()
                self.wait(1500)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(1500)
                #if not self.find( "bstatusorcamento", matching=0.97, waiting_time=10000):
                 #   self.not_found("bstatusorcamento")
                #elf.click_relative(357, 26)
                #if not self.find( "selecionarstatusabertaeminclusao", matching=0.97, waiting_time=10000):
                #    self.not_found("selecionarstatusabertaeminclusao")
                #self.click()   
                self.enter()         
                self.wait(1500)
                if not self.find( "bcpagorcamento", matching=0.97, waiting_time=10000):
                    self.not_found("bcpagorcamento")
                self.click_relative(47, 28)
                self.backspace()
                self.enter()
                self.wait(1500)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(1500)
                if not self.find( "bclienteorcamento", matching=0.97, waiting_time=10000):
                    self.not_found("bclienteorcamento")
                self.click_relative(193, 41)
                self.backspace()
                self.enter()
                self.wait(1500)
                self.type_down()
                self.wait(1500)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(1500)
                self.tab()
                self.tab()
                #
                #
                #
                #
                #
                #
                if not bot.find( "fatu_btn_vendas_vendedor_orcam", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_vendas_vendedor_orcam")
                bot.click_relative(58, 29)
                self.wait(1500)
                self.enter()
                self.wait(5000)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(1500)
                self.tab()
                self.tab()
                if not self.find( "brotaorcamento", matching=0.97, waiting_time=10000):
                    self.not_found("brotaorcamento")
                self.click_relative(53, 27)
                self.wait(1500)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(1500)
                if not self.find( "bclassorcamento", matching=0.97, waiting_time=10000):
                    self.not_found("bclassorcamento")
                self.click_relative(53, 24)
                self.wait(1500)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(1500)
                self.tab()
                self.tab()
                if not self.find( "bcimorcamento", matching=0.97, waiting_time=10000):
                    self.not_found("bcimorcamento")
                self.click_relative(62, 26)
                self.enter()
                self.wait(6000)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(2500)
                
                x=0
                while x<15:
                    if not self.find( "integracaoloop", matching=0.97, waiting_time=10000):
                        self.not_found("integracaoloop")
                    self.click_relative(89, 25)
                    self.type_down()
                    self.enter()
                    x=x+1
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                
                if not self.find( "aba1p2inclusaoorcamento", matching=0.97, waiting_time=10000):
                    self.not_found("aba1p2inclusaoorcamento")
                self.click()
                if not self.find( "brecebimentoacordado", matching=0.97, waiting_time=10000):
                    self.not_found("brecebimentoacordado")
                self.click_relative(50, 25)
                self.wait(1500)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(1500)
                if not self.find( "bpessoacontado", matching=0.97, waiting_time=10000):
                    self.not_found("bpessoacontado")
                self.click_relative(63, 25)
                self.wait(1500)
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "btransportador", matching=0.97, waiting_time=10000):
                    self.not_found("btransportador")
                self.click_relative(196, 45)
                self.enter()
                self.wait(2500)
                self.type_down()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(1500)
                if not self.find( "fretepcontaloop", matching=0.97, waiting_time=10000):
                    self.not_found("fretepcontaloop")
                self.click_relative(263, 43)
                self.type_up()
                self.enter()
                x=0
                while x<5:
                    if not self.find( "fretepcontaloop", matching=0.97, waiting_time=10000):
                        self.not_found("fretepcontaloop")
                    self.click_relative(263, 43)
                    self.type_down()
                    self.enter()
                    x=x+1
                self.type_keys_with_interval(1,'123')
                self.tab()
                self.type_keys_with_interval(1,'123')
                self.tab()
                self.type_keys_with_interval(1,'t1!')
                self.tab()
                self.type_keys_with_interval(1,'t1!')
                self.tab()
                self.type_keys_with_interval(1,'t1!')
                self.tab()
                self.type_keys_with_interval(1,'123')
                self.wait(1000)
                if not bot.find( "fatu_vendas_orcamento_2_movto_itens", matching=0.97, waiting_time=10000):
                    not_found("fatu_vendas_orcamento_2_movto_itens")
                bot.click()
                if not self.find( "addregistroaba2reqcompras", matching=0.97, waiting_time=10000):
                    self.not_found("addregistroaba2reqcompras")
                self.click()
                if not self.find( "buscaritensreqcompras", matching=0.97, waiting_time=10000):
                    self.not_found("buscaritensreqcompras")
                self.click_relative(10, 31)
                self.type_keys_with_interval(1,'agulha gengival')
                self.enter()
                self.type_down()
                self.type_down()
                self.type_down()
                self.type_down()
                self.wait(500)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # self.wait(500)
                # if not self.find( "quantidade_lancitens", matching=0.97, waiting_time=10000):
                #     self.not_found("quantidade_lancitens")
                # self.click_relative(336, 280)
                # self.backspace()
                # self.enter()
                # x=0
                # while x<31:
                #     self.type_down()
                #     x=x+1
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # self.wait(500)
                
                if not self.find( "quantidadeitens_teste", matching=0.97, waiting_time=10000):
                    self.not_found("quantidadeitens_teste")
                self.click_relative(105, 218)
                self.type_keys_with_interval(1,'1')
                if not self.find( "botaoconfirmaritensreqcompras", matching=0.97, waiting_time=10000):
                    self.not_found("botaoconfirmaritensreqcompras")
                self.click()
                self.wait(3000)
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                #if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                #    self.not_found("retornarpe")
                #self.click()
                
                if not self.find( "a2p2_orcamento", matching=0.97, waiting_time=10000):
                    self.not_found("a2p2_orcamento")
                self.click_relative(83, 136)
                if not self.find( "addregistroaba2reqcompras", matching=0.97, waiting_time=10000):
                    self.not_found("addregistroaba2reqcompras")
                self.click()
                if not self.find( "b_a2p2_servico_orcamento", matching=0.97, waiting_time=10000):
                    self.not_found("b_a2p2_servico_orcamento")
                self.click_relative(78, 177)
                self.wait(1500)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(1500)
                
                if not bot.find( "fatu_vendas_orcamento_classificacao_rel", matching=0.97, waiting_time=10000):
                    not_found("fatu_vendas_orcamento_classificacao_rel")
                bot.click_relative(56, 25)
                self.wait(1500)
                self.enter()
                self.wait(2000)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(1500)
                if not self.find( "b_a2p2_centroCusto_orcamento", matching=0.97, waiting_time=10000):
                    self.not_found("b_a2p2_centroCusto_orcamento")
                self.click_relative(1018, 178)
                self.enter()
                self.wait(1500)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(1500)
                if not self.find( "valorunitario_a2p2_orcamento", matching=0.97, waiting_time=10000):
                    self.not_found("valorunitario_a2p2_orcamento")
                self.click_relative(701, 174)
                self.type_keys_with_interval(1,'123')
                self.tab()
                if not self.find( "gravarregistroaba3", matching=0.97, waiting_time=10000):
                    self.not_found("gravarregistroaba3")
                self.click()
                if not self.find( "cancelarregistroaba3", matching=0.97, waiting_time=10000):
                    self.not_found("cancelarregistroaba3")
                self.click()
                if not self.find( "excluirRegistro_a2p2_orcamento", matching=0.97, waiting_time=10000):
                    self.not_found("excluirRegistro_a2p2_orcamento")
                self.click_relative(-8, 183)
                #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                #    self.not_found("simexcluirrs")
                #self.click()
                self.enter()
                if not self.find( "aba3inclusaoorcamento", matching=0.97, waiting_time=10000):
                    self.not_found("aba3inclusaoorcamento")
                self.click()
                if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                    self.not_found("salvarrs")
                self.click()
                self.enter()
                self.wait(1500)
                self.enter()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                self.wait(1000)
                if not bot.find( "fatu_vendas_btn_editar_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_vendas_btn_editar_2411")
                bot.click()
                self.wait(3000)
                if not self.find( "analise_orcamento", matching=0.97, waiting_time=10000):
                    self.not_found("analise_orcamento")
                self.click()
                
                if not self.find( "requisitar_orcamento", matching=0.97, waiting_time=10000):
                    self.not_found("requisitar_orcamento")
                self.click()
                if not self.find( "retornaropcaogeracao", matching=0.97, waiting_time=10000):
                    self.not_found("retornaropcaogeracao")
                self.click_relative(24, 34)
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()
                #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                #    self.not_found("simexcluirrs")
                #self.click()
                self.enter()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                
                                ####---INCLUIR PEDIDOS DE VENDA---####
                #                  
                # if not self.find( "aba1pedidosdevendainclusao", matching=0.97, waiting_time=10000):
                #     self.not_found("aba1pedidosdevendainclusao")
                # self.click()                            
                # if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                #     not_found("fatu_btn_incluir_opc_1_2411")
                # bot.click()
                # if not self.find( "bcoporcamento", matching=0.97, waiting_time=10000):
                #     self.not_found("bcoporcamento")
                # self.click_relative(54, 26)
                # self.backspace()
                # self.enter()
                # self.wait(500)
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # self.wait(500)
                # if not self.find( "bstatusorcamento", matching=0.97, waiting_time=10000):
                #     self.not_found("bstatusorcamento")
                # self.click_relative(357, 26)
                # if not self.find( "selecionarstatusabertaeminclusao", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarstatusabertaeminclusao")
                # self.click()            
                # self.wait(500)
                # if not self.find( "bcpagorcamento", matching=0.97, waiting_time=10000):
                #     self.not_found("bcpagorcamento")
                # self.click_relative(47, 28)
                # self.backspace()
                # self.enter()
                # self.wait(500)
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # self.wait(500)
                # if not self.find( "bclienteorcamento", matching=0.97, waiting_time=10000):
                #     self.not_found("bclienteorcamento")
                # self.click_relative(193, 41)
                # self.backspace()
                # self.enter()
                # self.type_down()
                # self.wait(500)
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # self.wait(500)
                # if not self.find( "bvendorcamento", matching=0.97, waiting_time=10000):
                #     self.not_found("bvendorcamento")
                # self.click_relative(56, 27)
                # self.wait(500)
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # self.wait(500)
                # self.tab()
                # self.tab()
                # if not self.find( "brotaorcamento", matching=0.97, waiting_time=10000):
                #     self.not_found("brotaorcamento")
                # self.click_relative(53, 27)
                # self.wait(500)
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # self.wait(500)
                # if not self.find( "bclassorcamento", matching=0.97, waiting_time=10000):
                #     self.not_found("bclassorcamento")
                # self.click_relative(53, 24)
                # self.wait(500)
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # self.wait(500)
                # self.tab()
                # self.tab()
                # if not self.find( "bcimorcamento", matching=0.97, waiting_time=10000):
                #     self.not_found("bcimorcamento")
                # self.click_relative(62, 26)
                # self.enter()
                # self.wait(3500)
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # self.wait(500)
                # x=0
                # while x<15:
                #     if not self.find( "integracaoloop", matching=0.97, waiting_time=10000):
                #         self.not_found("integracaoloop")
                #     self.click_relative(89, 25)
                #     self.type_down()
                #     self.enter()
                #     x=x+1
                # self.type_keys_with_interval(1,'te12!@')
                # self.tab()
                # self.type_keys_with_interval(1,'te12!@')
                # self.tab()
                # self.type_keys_with_interval(1,'te12!@')
                # self.tab()
                
                # if not self.find( "aba1p2inclusaoorcamento", matching=0.97, waiting_time=10000):
                #     self.not_found("aba1p2inclusaoorcamento")
                # self.click()
                # if not self.find( "brecebimentoacordado", matching=0.97, waiting_time=10000):
                #     self.not_found("brecebimentoacordado")
                # self.click_relative(50, 25)
                # self.wait(500)
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # self.wait(500)
                # if not self.find( "bpessoacontado", matching=0.97, waiting_time=10000):
                #     self.not_found("bpessoacontado")
                # self.click_relative(63, 25)
                # self.wait(500)
                # if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                #     self.not_found("retornarfim")
                # self.click()
                # if not self.find( "btransportador", matching=0.97, waiting_time=10000):
                #     self.not_found("btransportador")
                # self.click_relative(196, 45)
                # self.enter()
                # self.wait(5000)
                # self.type_down()
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # self.wait(500)
                # if not self.find( "fretepcontaloop", matching=0.97, waiting_time=10000):
                #     self.not_found("fretepcontaloop")
                # self.click_relative(263, 43)
                # self.type_up()
                # self.enter()
                # x=0
                # while x<5:
                #     if not self.find( "fretepcontaloop", matching=0.97, waiting_time=10000):
                #         self.not_found("fretepcontaloop")
                #     self.click_relative(263, 43)
                #     self.type_down()
                #     self.enter()
                #     x=x+1
                # self.type_keys_with_interval(1,'123')
                # self.tab()
                # self.type_keys_with_interval(1,'123')
                # self.tab()
                # self.type_keys_with_interval(1,'t1!')
                # self.tab()
                # self.type_keys_with_interval(1,'t1!')
                # self.tab()
                # self.type_keys_with_interval(1,'t1!')
                # self.tab()
                # self.type_keys_with_interval(1,'123')
                
                # if not self.find( "aba2inclusaoorcamento", matching=0.97, waiting_time=10000):
                #     self.not_found("aba2inclusaoorcamento")
                # self.click()
                # if not self.find( "addregistroaba2reqcompras", matching=0.97, waiting_time=10000):
                #     self.not_found("addregistroaba2reqcompras")
                # self.click()
                
                # if not self.find( "buscaritensreqcompras", matching=0.97, waiting_time=10000):
                #     self.not_found("buscaritensreqcompras")
                # self.click_relative(10, 31)
                # self.type_keys_with_interval(1,'104455')
                # self.enter()
                # self.wait(500)
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # self.wait(500)
                # self.type_keys_with_interval(1,'1')
                # if not self.find( "botaoconfirmaritensreqcompras", matching=0.97, waiting_time=10000):
                #     self.not_found("botaoconfirmaritensreqcompras")
                # self.click()
                # self.wait(3000)
                # self.type_right()
                # self.enter()
                # self.wait(1000)
                # if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                #     self.not_found("retornarfim")
                # self.click()
                
                # if not self.find( "a2p2incluirorcamento", matching=0.97, waiting_time=10000):
                #     self.not_found("a2p2incluirorcamento")
                # self.click()
                # if not self.find( "addregistroaba2reqcompras", matching=0.97, waiting_time=10000):
                #     self.not_found("addregistroaba2reqcompras")
                # self.click()
                # if not self.find( "bservicoa2p2orc", matching=0.97, waiting_time=10000):
                #     self.not_found("bservicoa2p2orc")
                # self.click_relative(28, 50)
                # self.wait(500)
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # self.wait(500)
                # self.enter()
                # if not self.find( "bclassa2p2orc", matching=0.97, waiting_time=10000):
                #     self.not_found("bclassa2p2orc")
                # self.click_relative(24, 87)
                # self.enter()
                # self.wait(500)
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # self.wait(500)
                # if not self.find( "bcentrocustoa2p2orc", matching=0.97, waiting_time=10000):
                #     self.not_found("bcentrocustoa2p2orc")
                # self.click_relative(968, 51)
                # self.enter()
                # self.wait(500)
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # self.wait(500)
                # if not self.find( "valorunitarioa2p2orc", matching=0.97, waiting_time=10000):
                #     self.not_found("valorunitarioa2p2orc")
                # self.click_relative(679, 50)
                # self.type_keys_with_interval(1,'123')
                # self.tab()
                # if not self.find( "gravarregistroaba3", matching=0.97, waiting_time=10000):
                #     self.not_found("gravarregistroaba3")
                # self.click()
                # self.enter()
                # if not self.find( "cancelarregistroaba3", matching=0.97, waiting_time=10000):
                #     self.not_found("cancelarregistroaba3")
                # self.click()
                # if not self.find( "excluirregistroPVa2p2", matching=0.97, waiting_time=10000):
                #     self.not_found("excluirregistroPVa2p2")
                # self.click_relative(-58, 58)
                # self.enter()           
                # #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                # #    self.not_found("simexcluirrs")
                # #self.click()
                
                
                # if not self.find( "aba3inclusaoorcamento", matching=0.97, waiting_time=10000):
                #     self.not_found("aba3inclusaoorcamento")
                # self.click()
                # if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                #     self.not_found("salvarrs")
                # self.click()
                # if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                #     self.not_found("retornarfim")
                # self.click()
                # if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                #     self.not_found("localizarfim")
                # self.click()
                # if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                #     self.not_found("editarfim")
                # self.click()
                # if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                #     self.not_found("excluirrs")
                # self.click()
                # if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                #     self.not_found("simexcluirrs")
                # self.click()
                # if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                #     self.not_found("retornarfim")
                # self.click()
                # if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                #     self.not_found("localizarfim")
                # self.click()
                
                #                 ####---INCLUIR vendas2 BALCAO---####
                
                # if not self.find( "aba3inclusaoMV", matching=0.97, waiting_time=10000):
                #     self.not_found("aba3inclusaoMV")
                # self.click()
                # if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                #     not_found("fatu_btn_incluir_opc_1_2411")
                # bot.click()    
                # self.enter()
                
                #                 ####---INCLUIR CONDICIONAIS---####
                                
                # if not self.find( "aba4condicionaisMV", matching=0.97, waiting_time=10000):
                #     self.not_found("aba4condicionaisMV")
                # self.click()
                # if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                #     not_found("fatu_btn_incluir_opc_1_2411")
                # bot.click()    
                # self.enter()
                # if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                #     self.not_found("retornarfim")
                # self.click()
                
                #                 ####---INCLUIR TRANSFERENCIAS---####
                                
                # if not self.find( "aba6transferenciasinclusaoMV", matching=0.97, waiting_time=10000):
                #     self.not_found("aba6transferenciasinclusaoMV")
                # self.click()
                # if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                #     not_found("fatu_btn_incluir_opc_1_2411")
                # bot.click()    
                # self.enter()
                # if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                #     self.not_found("retornarfim")
                # self.click()
                # if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                #     self.not_found("retornarfim")
                # self.click()
                # 
                #                 ####---INCLUIR AMOSTRA---####
                #               
                # if not self.find( "aba7amostraMV", matching=0.97, waiting_time=10000):
                #     self.not_found("aba7amostraMV")
                # self.click()
                # if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                #     not_found("fatu_btn_incluir_opc_1_2411")
                # bot.click()
                # if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                #     not_found("fatu_btn_incluir_opc_1_2411")
                # bot.click()
                # if not self.find( "bcoporcamento", matching=0.97, waiting_time=10000):
                #     self.not_found("bcoporcamento")
                # self.click_relative(54, 26)
                # self.backspace()
                # self.enter()
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # self.wait(500)
                # if not self.find( "bstatusorcamento", matching=0.97, waiting_time=10000):
                #     self.not_found("bstatusorcamento")
                # self.click_relative(357, 26)
                # if not self.find( "selecionarstatusabertaeminclusao", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarstatusabertaeminclusao")
                # self.click()            
                # self.wait(500)
                # if not self.find( "bcpagorcamento", matching=0.97, waiting_time=10000):
                #     self.not_found("bcpagorcamento")
                # self.click_relative(47, 28)
                # self.backspace()
                # self.enter()
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # self.wait(500)
                # if not self.find( "bclienteorcamento", matching=0.97, waiting_time=10000):
                #     self.not_found("bclienteorcamento")
                # self.click_relative(193, 41)
                # self.backspace()
                # self.enter()
                # self.type_down()
                # self.wait(500)
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # self.wait(500)
                # if not self.find( "bvendorcamento", matching=0.97, waiting_time=10000):
                #     self.not_found("bvendorcamento")
                # self.click_relative(56, 27)
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # self.wait(500)
                # self.tab()
                # self.tab()
                # if not self.find( "brotaorcamento", matching=0.97, waiting_time=10000):
                #     self.not_found("brotaorcamento")
                # self.click_relative(53, 27)
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # self.wait(500)
                # if not self.find( "bclassorcamento", matching=0.97, waiting_time=10000):
                #     self.not_found("bclassorcamento")
                # self.click_relative(53, 24)
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # self.wait(500)
                # self.tab()
                # self.tab()
                # if not self.find( "bcimorcamento", matching=0.97, waiting_time=10000):
                #     self.not_found("bcimorcamento")
                # self.click_relative(62, 26)
                # self.enter()
                # self.wait(3500)
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # self.wait(500)
                # x=0
                # while x<15:
                #     if not self.find( "integracaoloop", matching=0.97, waiting_time=10000):
                #         self.not_found("integracaoloop")
                #     self.click_relative(89, 25)
                #     self.type_down()
                #     self.enter()
                #     x=x+1
                # self.type_keys_with_interval(1,'te12!@')
                # self.tab()
                # self.type_keys_with_interval(1,'te12!@')
                # self.tab()
                # self.type_keys_with_interval(1,'te12!@')
                # self.tab()
                
                # if not self.find( "aba1p2inclusaoorcamento", matching=0.97, waiting_time=10000):
                #     self.not_found("aba1p2inclusaoorcamento")
                # self.click()
                # if not self.find( "brecebimentoacordado", matching=0.97, waiting_time=10000):
                #     self.not_found("brecebimentoacordado")
                # self.click_relative(50, 25)
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # self.wait(500)
                # if not self.find( "bpessoacontado", matching=0.97, waiting_time=10000):
                #     self.not_found("bpessoacontado")
                # self.click_relative(63, 25)
                # if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                #     self.not_found("retornarfim")
                # self.click()
                # if not self.find( "btransportador", matching=0.97, waiting_time=10000):
                #     self.not_found("btransportador")
                # self.click_relative(196, 45)
                # self.enter()
                # self.wait(2500)
                # self.type_down()
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # self.wait(500)
                # if not self.find( "fretepcontaloop", matching=0.97, waiting_time=10000):
                #     self.not_found("fretepcontaloop")
                # self.click_relative(263, 43)
                # self.type_up()
                # self.enter()
                # x=0
                # while x<5:
                #     if not self.find( "fretepcontaloop", matching=0.97, waiting_time=10000):
                #         self.not_found("fretepcontaloop")
                #     self.click_relative(263, 43)
                #     self.type_down()
                #     self.enter()
                #     x=x+1
                # self.type_keys_with_interval(1,'123')
                # self.tab()
                # self.type_keys_with_interval(1,'123')
                # self.tab()
                # self.type_keys_with_interval(1,'t1!')
                # self.tab()
                # self.type_keys_with_interval(1,'t1!')
                # self.tab()
                # self.type_keys_with_interval(1,'t1!')
                # self.tab()
                # self.type_keys_with_interval(1,'123')
                
                # if not self.find( "aba2inclusaoorcamento", matching=0.97, waiting_time=10000):
                #     self.not_found("aba2inclusaoorcamento")
                # self.click()
                # if not self.find( "addregistroaba2reqcompras", matching=0.97, waiting_time=10000):
                #     self.not_found("addregistroaba2reqcompras")
                # self.click()
                # if not self.find( "buscaritensreqcompras", matching=0.97, waiting_time=10000):
                #     self.not_found("buscaritensreqcompras")
                # self.click_relative(10, 31)
                # self.type_keys_with_interval(1,'104455')
                # self.enter()
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # self.wait(500)
                # self.type_keys_with_interval(1,'1')
                # if not self.find( "botaoconfirmaritensreqcompras", matching=0.97, waiting_time=10000):
                #     self.not_found("botaoconfirmaritensreqcompras")
                # self.click()
                # self.wait(3000)
                # self.type_right()
                # self.enter()
                # self.wait(1000)
                # if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                #     self.not_found("retornarfim")
                # self.click()
                
                # if not self.find( "a2p2incluirorcamento", matching=0.97, waiting_time=10000):
                #     self.not_found("a2p2incluirorcamento")
                # self.click()
                # if not self.find( "addregistroaba2reqcompras", matching=0.97, waiting_time=10000):
                #     self.not_found("addregistroaba2reqcompras")
                # self.click()
                # if not self.find( "bservicoa2p2orc", matching=0.97, waiting_time=10000):
                #     self.not_found("bservicoa2p2orc")
                # self.click_relative(28, 50)
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # self.wait(500)
                # if not self.find( "bclassa2p2orc", matching=0.97, waiting_time=10000):
                #     self.not_found("bclassa2p2orc")
                # self.click_relative(24, 87)
                # self.enter()
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # self.wait(500)
                # if not self.find( "bcentrocustoa2p2orc", matching=0.97, waiting_time=10000):
                #     self.not_found("bcentrocustoa2p2orc")
                # self.click_relative(968, 51)
                # self.enter()
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # self.wait(500)
                # if not self.find( "valorunitarioa2p2orc", matching=0.97, waiting_time=10000):
                #     self.not_found("valorunitarioa2p2orc")
                # self.click_relative(679, 50)
                # self.type_keys_with_interval(1,'123')
                # self.tab()
                # if not self.find( "gravarregistroaba3", matching=0.97, waiting_time=10000):
                #     self.not_found("gravarregistroaba3")
                # self.click()
                # if not self.find( "cancelarregistroaba3", matching=0.97, waiting_time=10000):
                #     self.not_found("cancelarregistroaba3")
                # self.click()
                # if not self.find( "excluirservicoamostraa2p2", matching=0.97, waiting_time=10000):
                #     self.not_found("excluirservicoamostraa2p2")
                # self.click_relative(-56, 55)
                # if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                #     self.not_found("simexcluirrs")
                # self.click()
                
                # if not self.find( "aba3inclusaoorcamento", matching=0.97, waiting_time=10000):
                #     self.not_found("aba3inclusaoorcamento")
                # self.click()
                # if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                #     self.not_found("salvarrs")
                # self.click()
                # if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                #     self.not_found("retornarfim")
                # self.click()
                # if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                #     self.not_found("localizarfim")
                # self.click()
                # if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                #     self.not_found("editarfim")
                # self.click()
                # if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                #     self.not_found("excluirrs")
                # self.click()
                # if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                #     self.not_found("simexcluirrs")
                # self.click()
                # if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                #     self.not_found("retornarfim")
                # self.click()
                # if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                #     self.not_found("localizarfim")
                # self.click()
                
                # if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                #     self.not_found("retornarfim")
                # self.click()
                # 
                                ####---EMISSAO DE NOTA FISCAL---####
                                ####################################
                if not self.find( "vendas2", matching=0.97, waiting_time=10000):
                    self.not_found("vendas2")
                self.click()
                if not self.find( "emissaonotafiscal", matching=0.97, waiting_time=10000):
                    self.not_found("emissaonotafiscal")
                self.click()
                self.wait(3000)
                self.enter()
                #if not self.find( "periodomovimentodenotas", matching=0.97, waiting_time=10000):
                #    self.not_found("periodomovimentodenotas")
                #self.double_click_relative(323, 111)
                #if not self.find( "carregardiaMN", matching=0.97, waiting_time=10000):
                #    self.not_found("carregardiaMN")
                #self.click()
                #if not self.find( "carregardiaatualMN", matching=0.97, waiting_time=10000):
                #    self.not_found("carregardiaatualMN")
                #self.click()
                self.tab()
                self.type_up()
                x=0
                while x<3:
                    self.type_down()
                    x=x+1
                self.type_up()
                self.type_up()
                if not self.find( "clienteMN", matching=0.97, waiting_time=10000):
                    self.not_found("clienteMN")
                self.click()
                if not bot.find( "fatu_vendas_btn_orcamento_cliente_buscar", matching=0.97, waiting_time=10000):
                    not_found("fatu_vendas_btn_orcamento_cliente_buscar")
                bot.click_relative(19, 29)
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                self.wait(3000)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                
                self.wait(3500)
                # MOUSE PARANDO EM CIMA, APENAS CLICAR

                #if not bot.find( "fatu_vendas_btn_incluir_mov_notas_2411", matching=0.97, waiting_time=10000):
                #    not_found("fatu_vendas_btn_incluir_mov_notas_2411")
                bot.click()
                
                                ####---INCLUSAO NOTA FISCAL---####
                                
                self.tab()
                self.type_keys_with_interval(1,'1')
                #self.tab()
                self.wait(500)
                x=0
                while x<6:
                    self.tab()
                    x=x+1
                self.type_keys_with_interval(1,'1111')
                self.wait(1500)
                self.tab()
                self.type_keys_with_interval(1,'123')
                self.wait(1500)
                self.tab()
                x=0
                while x<3:
                    self.type_down()
                    x=x+1
                x=0
                while x<3:
                    self.type_up()
                    x=x+1
                self.wait(1500)
                self.tab()
                self.wait(1500)
                self.type_up()
                x=0
                while x<4:
                    self.type_down()
                    x=x+1
                x=0
                while x<4:
                    self.type_up()
                    x=x+1
                self.wait(500)
                self.tab()
                self.wait(1500)
                x=0
                while x<8:
                    self.type_down()
                    x=x+1
                self.wait(500)
                x=0
                while x<8:
                    self.type_up()
                    x=x+1
                if not self.find( "b_cfopNF", matching=0.97, waiting_time=10000):
                    self.not_found("b_cfopNF")
                self.click_relative(55, 24)
                self.backspace()
                self.type_keys_with_interval(1,'5.102')
                self.enter()
                self.wait(500)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "b_condicaopagamentoNF", matching=0.97, waiting_time=10000):
                    self.not_found("b_condicaopagamentoNF")
                self.click_relative(42, 26)
                self.backspace()
                self.enter()
                self.wait(1500)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(3000)
                if not self.find( "b_localdeestoqueNF", matching=0.97, waiting_time=10000):
                    self.not_found("b_localdeestoqueNF")
                self.click_relative(41, 26)
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "b_clienteNF", matching=0.97, waiting_time=10000):
                    self.not_found("b_clienteNF")
                self.click_relative(193, 39)
                self.backspace()
                #self.type_keys_with_interval(1,'18')
                self.enter()
                self.wait(2000)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(1500)
                self.tab()
                self.tab()
                if not self.find( "b_vendedorNF", matching=0.97, waiting_time=10000):
                    self.not_found("b_vendedorNF")
                self.click_relative(68, 26)
                self.wait(1500)
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                self.wait(1500)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(1500)
                self.tab()
                self.tab()
                if not self.find( "b_rotaNF", matching=0.97, waiting_time=10000):
                    self.not_found("b_rotaNF")
                self.click_relative(65, 22)
                self.enter()
                self.wait(500)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "b_classificacaoNF", matching=0.97, waiting_time=10000):
                    self.not_found("b_classificacaoNF")
                self.click_relative(64, 23)
                self.backspace()
                self.enter()
                self.wait(500)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.tab()
                self.tab()
                if not self.find( "b_CImarketplaceNF", matching=0.97, waiting_time=10000):
                    self.not_found("b_CImarketplaceNF")
                self.click_relative(65, 25)
                self.enter()
                self.wait(1500)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.tab()
                self.tab()
                self.type_keys_with_interval(1,'123')
                self.tab()
                self.type_keys_with_interval(1,'t1!')
                self.tab()
                self.type_keys_with_interval(1,'t1!')
                self.tab()    
                self.type_keys_with_interval(1,'t1!')
                self.tab()
                self.tab()
                self.type_keys_with_interval(1,'t1!')
                self.tab()
                self.type_keys_with_interval(1,'t1!')
                if not self.find( "a1p2NF", matching=0.97, waiting_time=10000):
                    self.not_found("a1p2NF")
                self.click()
                if not self.find( "b_transportadorNF", matching=0.97, waiting_time=10000):
                    self.not_found("b_transportadorNF")
                self.click_relative(197, 43)
                self.enter()
                self.wait(500)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "i_placaa1p2NF", matching=0.97, waiting_time=10000):
                    self.not_found("i_placaa1p2NF")
                self.click_relative(2, 227)
                self.backspace()
                self.backspace()
                self.type_keys_with_interval(1,'abc1234')
                self.tab()
                self.type_keys_with_interval(1,'abc1234')
                self.tab()
                x=0
                while x<28:
                    self.type_up()
                    x=x+1
                self.tab()
                self.type_up()
                x=0
                while x<5:
                    self.type_down()
                    x=x+1
                x=0
                while x<5:
                    self.type_up()
                    x=x+1
                self.tab()
                self.type_keys_with_interval(1,'123')
                self.tab()
                self.type_keys_with_interval(1,'123')
                self.tab()    
                self.type_keys_with_interval(1,'t1!')
                self.tab()
                self.type_keys_with_interval(1,'t1!')
                self.tab()
                self.type_keys_with_interval(1,'t1!')
                self.tab()
                self.type_keys_with_interval(1,'123')
                self.tab()
                self.type_keys_with_interval(1,'123')
                
                
                if not self.find( "a1p3NF", matching=0.97, waiting_time=10000):
                    self.not_found("a1p3NF")
                self.click()
                if not self.find( "a1p4NF", matching=0.97, waiting_time=10000):
                    self.not_found("a1p4NF")
                self.click()
                
                                ####---ABA2 NOTA FISCAL---####
                                
                if not self.find( "a2NF", matching=0.97, waiting_time=10000):
                    self.not_found("a2NF")
                self.click()
                if not self.find( "ir_a2p1NF", matching=0.97, waiting_time=10000):
                    self.not_found("ir_a2p1NF")
                self.click()
                if not self.find( "buscaritensreqcompras", matching=0.97, waiting_time=10000):
                    self.not_found("buscaritensreqcompras")
                self.click_relative(10, 31)
                self.type_keys_with_interval(1,'agulha gengival')
                self.enter()
                self.type_down()
                self.type_down()
                self.type_down()
                self.type_down()
                self.wait(500)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # self.wait(500)
                # if not self.find( "quantidade_lancitens", matching=0.97, waiting_time=10000):
                #     self.not_found("quantidade_lancitens")
                # self.click_relative(336, 280)
                # self.backspace()
                # self.enter()
                # x=0
                # while x<31:
                #     self.type_down()
                #     x=x+1
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # self.wait(500)
                
                self.type_keys_with_interval(1,'1')
                if not self.find( "botaoconfirmaritensreqcompras", matching=0.97, waiting_time=10000):
                    self.not_found("botaoconfirmaritensreqcompras")
                self.click()
                self.wait(3000)
                if not self.find( "qntdmovimentarlotes", matching=0.97, waiting_time=10000):
                    self.not_found("qntdmovimentarlotes")
                self.double_click_relative(121, 231)
                self.backspace()
                self.backspace()
                self.backspace()
                self.backspace()
                self.type_keys_with_interval(1,'1')
                self.tab()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(1500)
                self.tab()
                self.wait(1500)
                self.type_keys_with_interval(1,'5206')
                self.wait(1500)
                self.tab()
                self.tab()
                self.tab()
                self.tab()
                self.tab()
                self.type_keys_with_interval(1,'00184')
                x=0
                while x<13:
                    self.tab()
                    x=x+1
                x=0
                while x<6:
                    self.type_down()
                    x=x+1
                self.tab()
                x=0
                while x<21:
                    self.type_down()
                    x=x+1
                self.tab()
                x=0
                while x<4:
                    self.type_down()
                    x=x+1
                if not self.find( "valoripiiss", matching=0.97, waiting_time=10000):
                    self.not_found("valoripiiss")
                self.click_relative(336, 41)
                self.tab()
                x=0
                while x<6:
                    self.type_down()
                    x=x+1
                self.tab()
                x=0
                while x<14:
                    self.type_down()
                    x=x+1
                if not self.find( "valorpisDII", matching=0.97, waiting_time=10000):
                    self.not_found("valorpisDII")
                self.click_relative(338, 94)
                self.tab()
                x=0
                while x<6:
                    self.type_down()
                    x=x+1
                self.tab()
                x=0
                while x<35:
                    self.type_down()
                    x=x+1
                self.tab()
                self.tab()
                if not self.find( "valorcofinsDII", matching=0.97, waiting_time=10000):
                    self.not_found("valorcofinsDII")
                self.click_relative(336, 148)
                self.tab()
                x=0
                while x<6:
                    self.type_down()
                    x=x+1
                self.tab()
                x=0
                while x<35:
                    self.type_down()
                    x=x+1
                
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                self.enter()
                self.wait(2000)
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()           
                self.enter()  
                if not self.find( "a2p2NF", matching=0.97, waiting_time=10000):
                    self.not_found("a2p2NF")
                self.click()
                if not self.find( "b_servicoa2p2NF", matching=0.97, waiting_time=10000):
                    self.not_found("b_servicoa2p2NF")
                self.click_relative(101, 230)
                self.enter()
                self.wait(500)
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                self.wait(500)
                self.tab()
                self.tab()
                self.type_keys_with_interval(1,'1')
                self.tab()
                self.type_keys_with_interval(1,'1')
                if not self.find( "a2p2NF", matching=0.97, waiting_time=10000):
                    self.not_found("a2p2NF")
                self.click()
                if not self.find( "b_classa2p2NF", matching=0.97, waiting_time=10000):
                    self.not_found("b_classa2p2NF")
                self.click_relative(94, 267)
                self.enter()
                self.wait(500)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "b_centrocustosa2p2NF", matching=0.97, waiting_time=10000):
                    self.not_found("b_centrocustosa2p2NF")
                self.click_relative(1038, 230)
                self.enter()
                self.wait(500)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "b_municipioa2p2NF", matching=0.97, waiting_time=10000):
                    self.not_found("b_municipioa2p2NF")
                self.click_relative(459, 266)
                self.enter()
                self.wait(500)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "gravara2p2NF", matching=0.97, waiting_time=10000):
                    self.not_found("gravara2p2NF")
                self.click_relative(1209, 270)
                self.enter()
                self.wait(2000)
                self.enter() 
                if not self.find( "salvardadosservicoimposto", matching=0.97, waiting_time=10000):
                    self.not_found("salvardadosservicoimposto")
                self.click()            
                self.enter()
                #self.enter()
                #self.enter()
                #if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                #    self.not_found("retornarpe")
                #self.click()
                if not self.find( "a2NF", matching=0.97, waiting_time=10000):
                    self.not_found("a2NF")
                self.click()  
                if not self.find( "cancelara2p2NF", matching=0.97, waiting_time=10000):
                    self.not_found("cancelara2p2NF")
                self.click()
                if not self.find( "apagara2p2NF", matching=0.97, waiting_time=10000):
                    self.not_found("apagara2p2NF")
                self.click_relative(-57, 33)
                #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                #    self.not_found("simexcluirrs")
                #self.click()
                self.enter()
                
                if not self.find( "aba3NF", matching=0.97, waiting_time=10000):
                    self.not_found("aba3NF")
                self.click()
                if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                    self.not_found("salvarrs")
                self.click()
                self.wait(1500)
                self.enter()
                if not self.find( "aba3NF", matching=0.97, waiting_time=10000):
                    self.not_found("aba3NF")
                self.click()
                self.enter()
                if not self.find( "ir_a2p1NF", matching=0.97, waiting_time=10000):
                    self.not_found("ir_a2p1NF")
                self.click()            
                if not self.find( "retornarconsulta", matching=0.97, waiting_time=10000):
                    self.not_found("retornarconsulta")
                self.click_relative(33, 44)
                self.wait(3000)
                self.enter()            
                # if not self.find( "finalizarNF", matching=0.97, waiting_time=10000):
                #     self.not_found("finalizarNF")
                # self.click_relative(64, -4)
                # self.wait(3000)
                # if not self.find( "finalizarNFeimprimir", matching=0.97, waiting_time=10000):
                #     self.not_found("finalizarNFeimprimir")
                # self.click()
                # self.wait(3000)
                # self.enter()
                # if not self.find( "quantidadeNFfinal", matching=0.97, waiting_time=10000):
                #     self.not_found("quantidadeNFfinal")
                # self.click_relative(397, 466)   
                # self.type_keys_with_interval(1,'1')
                # self.tab()
                # if not self.find( "finalizarNF", matching=0.97, waiting_time=10000):
                #     self.not_found("finalizarNF")
                # self.click()
                # self.wait(500)
                # if not self.find( "b_localcobrancaparcela", matching=0.97, waiting_time=10000):
                #     self.not_found("b_localcobrancaparcela")
                # self.click_relative(55, 45)
                # self.wait(500)
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # self.wait(500)
                # if not self.find( "b_classparcela", matching=0.97, waiting_time=10000):
                #     self.not_found("b_classparcela")
                # self.click_relative(55, 93)
                # self.wait(500)
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # self.wait(500)
                # if not self.find( "b_sacadorparcela", matching=0.97, waiting_time=10000):
                #     self.not_found("b_sacadorparcela")
                # self.click_relative(54, 138)
                # self.type_keys_with_interval(1,'0081260')
                # self.enter()
                # self.wait(500)
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # self.wait(500)
                # if not self.find( "b_tipopagamentoparcelas", matching=0.97, waiting_time=10000):
                #     self.not_found("b_tipopagamentoparcelas")
                # self.click_relative(57, 184)
                # self.wait(500)
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # self.wait(500)
                # if not self.find( "b_planofinanceiroparcelas", matching=0.97, waiting_time=10000):
                #     self.not_found("b_planofinanceiroparcelas")
                # self.click_relative(572, 45)
                # self.wait(500)
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # self.wait(500)
                # if not self.find( "b_operacaoparcelas", matching=0.97, waiting_time=10000):
                #     self.not_found("b_operacaoparcelas")
                # self.click_relative(537, 93)
                # self.wait(500)
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # self.wait(500)
                # if not self.find( "b_comissaoparcelas", matching=0.97, waiting_time=10000):
                #     self.not_found("b_comissaoparcelas")
                # self.click_relative(534, 137)
                # self.wait(500)
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # self.wait(500)
                # if not self.find( "continuarfinalizacaoNF", matching=0.97, waiting_time=10000):
                #     self.not_found("continuarfinalizacaoNF")
                # self.click()
                # if not self.find( "retornarfinanceirofinalNF", matching=0.97, waiting_time=10000):
                #     self.not_found("retornarfinanceirofinalNF")
                # self.click_relative(37, 45)
                # if not self.find( "retornarimpressaoNFfinal", matching=0.97, waiting_time=10000):
                #     self.not_found("retornarimpressaoNFfinal")
                # self.click_relative(30, 46)
                # self.wait(500)
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()
                #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                #    self.not_found("simexcluirrs")
                #self.click()
                self.enter()
                self.type_keys_with_interval(1,'Nota feita com teste automatizado')
                self.enter()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                self.wait(500)
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                                ####---ROMANEIOS DE SAIDA---####
                
                if not self.find( "vendas2", matching=0.97, waiting_time=10000):
                    self.not_found("vendas2")
                self.click()
                if not self.find( "romaneiosdesaida", matching=0.97, waiting_time=10000):
                    self.not_found("romaneiosdesaida")
                self.click()
                self.enter()
                if not self.find( "b_transportadorCMR", matching=0.97, waiting_time=10000):
                    self.not_found("b_transportadorCMR")
                self.click_relative(478, 88)
                self.type_keys_with_interval(1,'0081260')
                self.enter()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                self.tab()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                self.tab()
                self.tab()
                self.tab()
                self.type_keys_with_interval(1,'123')
                self.tab()
                self.type_up()
                self.type_up()
                self.tab()
                if not self.find( "b_transportador_inclusao", matching=0.97, waiting_time=10000):
                    self.not_found("b_transportador_inclusao")
                self.click_relative(81, 154)
                self.enter()
                self.wait(3000)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(1500)
                if not self.find( "b_rota_movRomaneios", matching=0.97, waiting_time=10000):
                    self.not_found("b_rota_movRomaneios")
                self.click_relative(64, 195)
                self.enter()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.tab()
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.type_keys_with_interval(1,'abc1234')
                self.tab()
                self.type_keys_with_interval(1,'abc1234')
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                    self.not_found("salvarrs")
                self.click()
                self.wait(500)
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                self.type_right()
                self.enter()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                #if not self.find( "s_busca_CMR", matching=0.97, waiting_time=10000):
                #    self.not_found("s_busca_CMR")
                #self.click()
                if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                    self.not_found("editarfim")
                self.click()
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()
                #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                #    self.not_found("simexcluirrs")
                #self.click()
                self.enter()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()            
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                                ####---EXPEDICAO---####
                                
                if not self.find( "vendas2", matching=0.97, waiting_time=10000):
                    self.not_found("vendas2")
                self.click()
                if not self.find( "expedicao", matching=0.97, waiting_time=10000):
                    self.not_found("expedicao")
                self.click()
                if not self.find( "expedicao2", matching=0.97, waiting_time=10000):
                    self.not_found("expedicao2")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()  
                if not self.find( "b_clienteMovExp", matching=0.97, waiting_time=10000):
                    self.not_found("b_clienteMovExp")
                self.click_relative(374, 83)
                self.enter()
                self.wait(1500)
                self.type_keys_with_interval(1,'0081260')
                self.enter()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                if not self.find( "exibiritenssim", matching=0.97, waiting_time=10000):
                    self.not_found("exibiritenssim")
                self.click()
                if not self.find( "exibiritensnao", matching=0.97, waiting_time=10000):
                    self.not_found("exibiritensnao")
                self.click()
                if not self.find( "situacaoloopMovExp", matching=0.97, waiting_time=10000):
                    self.not_found("situacaoloopMovExp")
                self.double_click_relative(64, 25)
                x=0
                while x<4:
                    self.type_up()
                    x=x+1
                x=0
                while x<4:
                    self.type_down()
                    x=x+1
                self.tab()
                x=0
                while x<2:
                    self.type_up()
                    x=x+1
                x=0            
                while x<2:
                    self.type_down()
                    x=x+1
                if not self.find( "a2selecaomovexp", matching=0.97, waiting_time=10000):
                    self.not_found("a2selecaomovexp")
                self.click()
                if not self.find( "b_itemselecao", matching=0.97, waiting_time=10000):
                    self.not_found("b_itemselecao")
                self.click_relative(12, 46)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "b_rotasMovEnt", matching=0.97, waiting_time=10000):
                    self.not_found("b_rotasMovEnt")
                self.click_relative(97, 124)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "situacao2movent", matching=0.97, waiting_time=10000):
                    self.not_found("situacao2movent")
                self.click()
                if not self.find( "situacao3movent", matching=0.97, waiting_time=10000):
                    self.not_found("situacao3movent")
                self.click()
                if not self.find( "situacao1movent", matching=0.97, waiting_time=10000):
                    self.not_found("situacao1movent")
                self.click()
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "addregistromovent", matching=0.97, waiting_time=10000):
                    self.not_found("addregistromovent")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()  
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                
                #if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                #    self.not_found("salvarrs")
                #self.click()
                self.wait(500)
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                    self.not_found("editarfim")
                self.click()
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()            
                #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                #    self.not_found("simexcluirrs")
                #self.click()
                self.enter()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()         
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()   
                        
                                ####---CONFERENCIA DE PEDIDOS---####
                                
                if not self.find( "vendas2", matching=0.97, waiting_time=10000):
                    self.not_found("vendas2")
                self.click()
                if not self.find( "expedicao", matching=0.97, waiting_time=10000):
                    self.not_found("expedicao")
                self.click()
                if not self.find( "conferenciadepedidos", matching=0.97, waiting_time=10000):
                    self.not_found("conferenciadepedidos")
                self.click()
                x=0
                while x<3:
                    self.tab()
                    self.space()
                    self.space()
                    x=x+1
                if not self.find( "b_itemConfPed", matching=0.97, waiting_time=10000):
                    self.not_found("b_itemConfPed")
                self.click_relative(117, 235)
                self.type_keys_with_interval(1,'agulha gengival')
                self.enter()
                self.type_down()
                self.type_down()
                self.type_down()
                self.type_down()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(1500)
                self.tab()
                self.tab()
                self.type_keys_with_interval(1,'123')
                self.tab()
                self.enter()
                if not self.find( "aba2confPed", matching=0.97, waiting_time=10000):
                    self.not_found("aba2confPed")
                self.double_click()
                if not self.find( "op_emb", matching=0.97, waiting_time=10000):
                    self.not_found("op_emb")
                self.click()
                if not self.find( "op_prvent", matching=0.97, waiting_time=10000):
                    self.not_found("op_prvent")
                self.click()
                if not self.find( "op_lanc", matching=0.97, waiting_time=10000):
                    self.not_found("op_lanc")
                self.click()
                if not self.find( "op_emi", matching=0.97, waiting_time=10000):
                    self.not_found("op_emi")
                self.click()
                if not self.find( "botãobuscar", matching=0.97, waiting_time=10000):
                    self.not_found("botãobuscar")
                self.click()
                self.wait(500)
                self.enter()
                self.wait(5000)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "situacaoconfped", matching=0.97, waiting_time=10000):
                    self.not_found("situacaoconfped")
                self.click_relative(541, 21)
                x=0
                while x<10:
                    self.type_down()
                    self.space()
                    x=x+1
                self.space()
                x=0
                while x<10:
                    self.type_up()
                    self.space()
                    x=x+1
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click() 
                
                                ####---CADASTRO DE ETIQUETAS---####
                                
                if not self.find( "vendas2", matching=0.97, waiting_time=10000):
                    self.not_found("vendas2")
                self.click()
                if not self.find( "expedicao", matching=0.97, waiting_time=10000):
                    self.not_found("expedicao")
                self.click()
                if not self.find( "cadastrodeetiquetas", matching=0.97, waiting_time=10000):
                    self.not_found("cadastrodeetiquetas")
                self.click()
                if not self.find( "incluirclaro", matching=0.97, waiting_time=10000):
                    self.not_found("incluirclaro")
                self.click()
                if not self.find( "cbmestre", matching=0.97, waiting_time=10000):
                    self.not_found("cbmestre")
                self.click_relative(7, 25)
                self.type_keys_with_interval(1,'123')
                self.tab()
                self.type_keys_with_interval(1,'123123')
                self.tab()
                if not self.find( "retornarclaro", matching=0.97, waiting_time=10000):
                    self.not_found("retornarclaro")
                self.click()
                if not self.find( "localizarclaro", matching=0.97, waiting_time=10000):
                    self.not_found("localizarclaro")
                self.click()
                if not self.find( "editarclaro", matching=0.97, waiting_time=10000):
                    self.not_found("editarclaro")
                self.click()            
                if not self.find( "excluiretiqueta", matching=0.97, waiting_time=10000):
                    self.not_found("excluiretiqueta")
                self.click_relative(2, 81)
                #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                #    self.not_found("simexcluirrs")
                #self.click()
                self.enter()
                if not self.find( "retornarclaro", matching=0.97, waiting_time=10000):
                    self.not_found("retornarclaro")
                self.click()
                if not self.find( "localizarclaro", matching=0.97, waiting_time=10000):
                    self.not_found("localizarclaro")
                self.click()
                if not self.find( "retornarclaro", matching=0.97, waiting_time=10000):
                    self.not_found("retornarclaro")
                self.click()
                
                                ####---LEITURA DE ETIQUETAS---####
                                
                if not self.find( "vendas2", matching=0.97, waiting_time=10000):
                    self.not_found("vendas2")
                self.click()
                if not self.find( "expedicao", matching=0.97, waiting_time=10000):
                    self.not_found("expedicao")
                self.click()
                if not self.find( "leituradeetiquetas", matching=0.97, waiting_time=10000):
                    self.not_found("leituradeetiquetas")
                self.click()
                self.type_keys_with_interval(1,'1')
                self.enter()
                if not self.find( "aba2confPed", matching=0.97, waiting_time=10000):
                    self.not_found("aba2confPed")
                self.double_click()
                if not self.find( "op_emb", matching=0.97, waiting_time=10000):
                    self.not_found("op_emb")
                self.click()
                if not self.find( "op_prvent", matching=0.97, waiting_time=10000):
                    self.not_found("op_prvent")
                self.click()
                if not self.find( "op_lanc", matching=0.97, waiting_time=10000):
                    self.not_found("op_lanc")
                self.click()
                if not self.find( "op_emi", matching=0.97, waiting_time=10000):
                    self.not_found("op_emi")
                self.click()
                if not self.find( "botãobuscar", matching=0.97, waiting_time=10000):
                    self.not_found("botãobuscar")
                self.click()
                self.wait(500)
                self.enter()
                self.wait(5000)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(1500)
                self.tab()
                self.backspace()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "gravarcodigo1", matching=0.97, waiting_time=10000):
                    self.not_found("gravarcodigo1")
                self.double_click_relative(176, 47)                       
                #if not self.find( "aba1etiquetasdepedidos", matching=0.97, waiting_time=10000):
                #    self.not_found("aba1etiquetasdepedidos")
                #self.click()
                self.wait(1000)                       
                if not self.find( "codigodebarrasaba1", matching=0.97, waiting_time=10000):
                    self.not_found("codigodebarrasaba1")
                self.double_click_relative(36, 283)            
                self.type_keys_with_interval(1,'123')
                self.tab()
                if not self.find( "gravarcodigos2", matching=0.97, waiting_time=10000):
                    self.not_found("gravarcodigos2")
                self.click()
                self.enter()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                self.enter()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                                ####---VENDAS PERDIDAS---####
                                
                if not self.find( "vendas2", matching=0.97, waiting_time=10000):
                    self.not_found("vendas2")
                self.click()
                if not self.find( "vendasperdidas", matching=0.97, waiting_time=10000):
                    self.not_found("vendasperdidas")
                self.click()
                self.enter()
                if not self.find( "aba2vendasperdidas", matching=0.97, waiting_time=10000):
                    self.not_found("aba2vendasperdidas")
                self.click()
                if not self.find( "a2_VP_vendedor", matching=0.97, waiting_time=10000):
                    self.not_found("a2_VP_vendedor")
                self.click_relative(66, 22)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                if not self.find( "a2_VP_motivo", matching=0.97, waiting_time=10000):
                    self.not_found("a2_VP_motivo")
                self.click_relative(65, 22)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                if not self.find( "a2_VP_item", matching=0.97, waiting_time=10000):
                    self.not_found("a2_VP_item")
                self.click_relative(64, 24)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                if not self.find( "a2_VP_cliente", matching=0.97, waiting_time=10000):
                    self.not_found("a2_VP_cliente")
                self.click_relative(65, 23)
                self.type_keys_with_interval(1,'0081260')
                self.enter()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                if not self.find( "b_item_perdido", matching=0.97, waiting_time=10000):
                    self.not_found("b_item_perdido")
                self.click_relative(75, 128)
                self.enter()
                self.wait(2500)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(1500)
                if not self.find( "b_cliente_perdidas", matching=0.97, waiting_time=10000):
                    self.not_found("b_cliente_perdidas")
                self.click_relative(72, 173)
                self.enter()
                self.wait(2500)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(1500)
                if not self.find( "b_vendedor_perdido", matching=0.97, waiting_time=10000):
                    self.not_found("b_vendedor_perdido")
                self.click_relative(69, 219)
                self.enter()
                self.wait(2500)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(1500)
                if not self.find( "b_motivo_perdido", matching=0.97, waiting_time=10000):
                    self.not_found("b_motivo_perdido")
                self.click_relative(427, 221)
                self.enter()
                self.wait(2500)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(1500)
                if not self.find( "op1_perdido", matching=0.97, waiting_time=10000):
                    self.not_found("op1_perdido")
                self.click_relative(399, 128)
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "op2_perdido", matching=0.97, waiting_time=10000):
                    self.not_found("op2_perdido")
                self.click_relative(401, 176)
                self.type_keys_with_interval(1,'te12!@')
                x=0
                while x<5:
                    self.tab()
                    x=x+1
                self.type_keys_with_interval(1,'123')
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                    self.not_found("salvarrs")
                self.click()
                self.wait(500)
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                    self.not_found("editarfim")
                self.click()
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()            
                #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                #    self.not_found("simexcluirrs")
                #self.click()
                self.enter()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()         
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                                ####---ORDEM DE SERVIÇO---####
                                
                if not self.find( "vendas2", matching=0.97, waiting_time=10000):
                    self.not_found("vendas2")
                self.click()
                if not self.find( "ordensdeservico", matching=0.97, waiting_time=10000):
                    self.not_found("ordensdeservico")
                self.click()
                if not self.find( "selecao_ordemservico", matching=0.97, waiting_time=10000):
                    self.not_found("selecao_ordemservico")
                self.click()
                if not self.find( "b_condpag_mos", matching=0.97, waiting_time=10000):
                    self.not_found("b_condpag_mos")
                self.click_relative(70, 193)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                if not self.find( "b_executor_mos", matching=0.97, waiting_time=10000):
                    self.not_found("b_executor_mos")
                self.click_relative(73, 241)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                if not self.find( "b_tipoos_mos", matching=0.97, waiting_time=10000):
                    self.not_found("b_tipoos_mos")
                self.click_relative(72, 287)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.enter()
                self.backspace()
                if not self.find( "b_recepcionista_mos", matching=0.97, waiting_time=10000):
                    self.not_found("b_recepcionista_mos")
                self.click_relative(463, 194)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                if not self.find( "b_servico_mos", matching=0.97, waiting_time=10000):
                    self.not_found("b_servico_mos")
                self.click_relative(462, 239)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                self.enter()
                if not self.find( "b_client_mos", matching=0.97, waiting_time=10000):
                    self.not_found("b_client_mos")
                self.click_relative(634, 122)
                self.type_keys_with_interval(1,'0081260')
                self.enter()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                self.tab()
                if not self.find( "s_cf", matching=0.97, waiting_time=10000):
                    self.not_found("s_cf")
                self.click()
                if not self.find( "s_nf", matching=0.97, waiting_time=10000):
                    self.not_found("s_nf")
                self.click()
                if not self.find( "s_docto", matching=0.97, waiting_time=10000):
                    self.not_found("s_docto")
                self.click()
                if not self.find( "periodo_mos", matching=0.97, waiting_time=10000):
                    self.not_found("periodo_mos")
                self.click_relative(32, 7)
                if not self.find( "periodo_ano", matching=0.97, waiting_time=10000):
                    self.not_found("periodo_ano")
                self.click()
                if not self.find( "periodo_ano_atual", matching=0.97, waiting_time=10000):
                    self.not_found("periodo_ano_atual")
                self.click()
                self.tab()
                self.type_down()
                self.type_down()
                self.type_up()
                self.type_up()
                if not self.find( "s_situ_andamento", matching=0.97, waiting_time=10000):
                    self.not_found("s_situ_andamento")
                self.click()
                if not self.find( "s_sit_finalizoficina", matching=0.97, waiting_time=10000):
                    self.not_found("s_sit_finalizoficina")
                self.click()
                if not self.find( "s_sit_fechadas", matching=0.97, waiting_time=10000):
                    self.not_found("s_sit_fechadas")
                self.click()
                if not self.find( "s_sit_canceladas", matching=0.97, waiting_time=10000):
                    self.not_found("s_sit_canceladas")
                self.click()
                if not self.find( "s_sit_todas", matching=0.97, waiting_time=10000):
                    self.not_found("s_sit_todas")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                self.enter()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                                ####---FRETES E RPA---####
                                
                if not self.find( "vendas2", matching=0.97, waiting_time=10000):
                    self.not_found("vendas2")
                self.click()
                if not self.find( "freteserpa", matching=0.97, waiting_time=10000):
                    self.not_found("freteserpa")
                self.click()
                if not self.find( "lancamentodefretes", matching=0.97, waiting_time=10000):
                    self.not_found("lancamentodefretes")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "aba2selecao_CMF", matching=0.97, waiting_time=10000):
                    self.not_found("aba2selecao_CMF")
                self.click()
                if not self.find( "b_transportador_CMF", matching=0.97, waiting_time=10000):
                    self.not_found("b_transportador_CMF")
                self.click_relative(508, 93)
                self.type_keys_with_interval(1,'0081260')
                self.enter()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                self.tab()
                if not self.find( "b_operacao_CMF", matching=0.97, waiting_time=10000):
                    self.not_found("b_operacao_CMF")
                self.click_relative(500, 168)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                self.tab()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                self.type_keys_with_interval(1,'874874')
                self.tab()
                self.type_keys_with_interval(1,'1')
                self.tab()
                self.type_keys_with_interval(1,'1')
                self.tab()
                x=0
                while x<9:
                    self.type_up()
                    x=x+1
                x=0
                while x<45:
                    self.type_down()
                    x=x+1
                self.tab()
                self.type_down()
                x=0
                while x<11:
                    self.type_up()
                    x=x+1
                self.tab()
                self.tab()
                self.tab()
                self.tab()
                if not self.find( "b_codoperacao_MFrete", matching=0.97, waiting_time=10000):
                    self.not_found("b_codoperacao_MFrete")
                self.click_relative(73, 157)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.tab()
                self.tab()
                self.tab()
                self.tab()
                self.type_keys_with_interval(1,'123')
                self.tab()
                self.type_keys_with_interval(1,'123')
                self.tab()
                self.tab()
                if not self.find( "b_transportador_Mfrete", matching=0.97, waiting_time=10000):
                    self.not_found("b_transportador_Mfrete")
                self.click_relative(202, 41)
                self.type_keys_with_interval(1,'0081260')
                self.enter()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "b_grupofiscal_Mfrete", matching=0.97, waiting_time=10000):
                    self.not_found("b_grupofiscal_Mfrete")
                self.click_relative(240, 202)
                self.type_keys_with_interval(1,'diferido')
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "b_centrocusto_Mfrete", matching=0.97, waiting_time=10000):
                    self.not_found("b_centrocusto_Mfrete")
                self.click_relative(840, 260)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                if not self.find( "b_municipiocoleta_Mfrete", matching=0.97, waiting_time=10000):
                    self.not_found("b_municipiocoleta_Mfrete")
                self.click_relative(69, 299)
                self.type_keys_with_interval(1,'guarapuava')
                self.tab()
                self.tab()
                self.tab()
                self.type_down()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "b_municipioentrega_Mfrete", matching=0.97, waiting_time=10000):
                    self.not_found("b_municipioentrega_Mfrete")
                self.click_relative(440, 306)
                self.type_keys_with_interval(1,'curitiba')
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.type_right()
                self.enter()
                self.tab()
                self.tab()
                x=0
                while x<4:
                    y=0
                    while y<3:
                        self.type_keys_with_interval(1,'123')
                        self.tab()
                        y=y+1
                    z=0
                    while z<6:
                        self.type_down()
                        z=z+1
                    self.tab()
                    self.tab()
                    x=x+1
                x=0
                while x<18:
                    self.type_down()
                    x=x+1
                x=0
                while x<14:
                    if not self.find( "sittribIPI", matching=0.97, waiting_time=10000):
                        self.not_found("sittribIPI")
                    self.click_relative(795, 43)
                    self.type_down()
                    self.enter()
                    x=x+1
                x=0
                while x<21:
                    if not self.find( "sittribICMS", matching=0.97, waiting_time=10000):
                        self.not_found("sittribICMS")
                    self.click_relative(792, 42)
                    self.type_down()
                    self.enter()
                    x=x+1
                x=0
                while x<4:
                    if not self.find( "sittribPIS", matching=0.97, waiting_time=10000):
                        self.not_found("sittribPIS")
                    self.click_relative(792, 44)                
                    self.type_down()
                    self.enter()
                    x=x+1
                x=0
                while x<33:
                    if not self.find( "sittribCOFINS", matching=0.97, waiting_time=10000):
                        self.not_found("sittribCOFINS")
                    self.click_relative(794, 43)
                    self.type_down()
                    self.enter()
                    x=x+1
                self.tab()
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                    self.not_found("salvarrs")
                self.click()
                self.wait(1000)
                self.type_right()
                self.enter()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                self.type_right()
                self.enter()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                self.enter()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                    self.not_found("editarfim")
                self.click()
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()            
                #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                #    self.not_found("simexcluirrs")
                #self.click()
                self.enter()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                self.enter()         
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                                ####---EMISSAO DE RPA---####
                                
                if not self.find( "vendas2", matching=0.97, waiting_time=10000):
                    self.not_found("vendas2")
                self.click()
                if not self.find( "freteserpa", matching=0.97, waiting_time=10000):
                    self.not_found("freteserpa")
                self.click()
                if not self.find( "emissaoderpa", matching=0.97, waiting_time=10000):
                    self.not_found("emissaoderpa")
                self.click()
                self.enter()
                if not self.find( "b_transportador_MRPA", matching=0.97, waiting_time=10000):
                    self.not_found("b_transportador_MRPA")
                self.click_relative(297, 86)
                self.type_keys_with_interval(1,'0081260')
                self.enter()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                self.tab()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                self.tab()
                if not self.find( "b_transportador_RPAtransporte", matching=0.97, waiting_time=10000):
                    self.not_found("b_transportador_RPAtransporte")
                self.click_relative(561, 87)
                self.enter()
                self.wait(1500)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.tab()
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                    self.not_found("salvarrs")
                self.click()
                self.wait(500)
                self.enter()
                if not self.find( "cancelar_RPAtransportadores", matching=0.97, waiting_time=10000):
                    self.not_found("cancelar_RPAtransportadores")
                self.click()
                self.enter()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                                ####---CHECAGEM DE LANCAMENTO---####
                                
                if not self.find( "vendas2", matching=0.97, waiting_time=10000):
                    self.not_found("vendas2")
                self.click()
                if not self.find( "checagemdelancamentos", matching=0.97, waiting_time=10000):
                    self.not_found("checagemdelancamentos")
                self.click()
                if not self.find( "b_calendario_checagemlanc", matching=0.97, waiting_time=10000):
                    self.not_found("b_calendario_checagemlanc")
                self.click_relative(33, 6)          
                if not self.find( "periodo_ano", matching=0.97, waiting_time=10000):
                    self.not_found("periodo_ano")
                self.click()
                if not self.find( "periodo_ano_atual", matching=0.97, waiting_time=10000):
                    self.not_found("periodo_ano_atual")
                self.click()
                if not self.find( "checagem_clancamento", matching=0.97, waiting_time=10000):
                    self.not_found("checagem_clancamento")
                self.click()
                self.wait(1500)
                if not self.find( "aba2_clancamento", matching=0.97, waiting_time=10000):
                    self.not_found("aba2_clancamento")
                self.click()
                if not self.find( "aba3_clancamento", matching=0.97, waiting_time=10000):
                    self.not_found("aba3_clancamento")
                self.click()
                if not self.find( "titulos_baixados_CL", matching=0.97, waiting_time=10000):
                    self.not_found("titulos_baixados_CL")
                self.click()
                if not self.find( "exibir_coperacao_CL", matching=0.97, waiting_time=10000):
                    self.not_found("exibir_coperacao_CL")
                self.click()
                if not self.find( "checagem_clancamento", matching=0.97, waiting_time=10000):
                    self.not_found("checagem_clancamento")
                self.click()
                self.wait(1500)
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                                ####---MOVIMENTO DE COMISSAO---####
                                
                if not self.find( "vendas2", matching=0.97, waiting_time=10000):
                    self.not_found("vendas2")
                self.click()
                if not self.find( "movimentodecomissao", matching=0.97, waiting_time=10000):
                    self.not_found("movimentodecomissao")
                self.click()
                self.enter()
                if not self.find( "aba2_MCI", matching=0.97, waiting_time=10000):
                    self.not_found("aba2_MCI")
                self.click()
                if not self.find( "b_vendedor_MCI", matching=0.97, waiting_time=10000):
                    self.not_found("b_vendedor_MCI")
                self.click_relative(380, 79)
                self.enter()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.tab()
                self.backspace()
                self.tab()
                if not self.find( "b_condpagamento_MCI", matching=0.97, waiting_time=10000):
                    self.not_found("b_condpagamento_MCI")
                self.double_click_relative(70, 150)
                self.wait(500)            
                self.enter()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.tab()
                self.backspace()
                self.tab()
                if not self.find( "b_cliente_MCI", matching=0.97, waiting_time=10000):
                    self.not_found("b_cliente_MCI")
                self.click_relative(70, 190)
                self.enter()
                self.wait(2000)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.tab()
                self.backspace()
                self.tab()
                if not self.find( "b_rota_MCI", matching=0.97, waiting_time=10000):
                    self.not_found("b_rota_MCI")
                self.click_relative(460, 190)
                self.enter()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                self.tab() 
                self.backspace()
                self.tab()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                self.tab()
                self.tab()
                self.type_down()
                self.type_up()
                if not self.find( "b_vendedor_MDC", matching=0.97, waiting_time=10000):
                    self.not_found("b_vendedor_MDC")
                self.click_relative(81, 158)
                self.enter()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "b_cliente_MDC", matching=0.97, waiting_time=10000):
                    self.not_found("b_cliente_MDC")
                self.click_relative(79, 195)
                self.enter()
                self.wait(2000)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.tab()
                self.tab()
                self.type_keys_with_interval(1,'123')
                self.tab()
                self.type_keys_with_interval(1,'123')
                self.tab()
                self.type_keys_with_interval(1,'123')
                self.tab()
                self.type_keys_with_interval(1,'123')
                if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                    self.not_found("salvarrs")
                self.click()
                self.wait(500)
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                    self.not_found("editarfim")
                self.click()
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()            
                #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                #    self.not_found("simexcluirrs")
                #self.click()
                self.enter()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()         
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                                ####---GERACAO DE ENQUETE---####
                
                if not self.find( "vendas2", matching=0.97, waiting_time=10000):
                    self.not_found("vendas2")
                self.click()
                if not self.find( "geracaodeenquetes", matching=0.97, waiting_time=10000):
                    self.not_found("geracaodeenquetes")
                self.click()
                if not self.find( "b_item_genq", matching=0.97, waiting_time=10000):
                    self.not_found("b_item_genq")
                self.click_relative(60, 22)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                self.tab()
                if not self.find( "b_clientefornecedor_genq", matching=0.97, waiting_time=10000):
                    self.not_found("b_clientefornecedor_genq")
                self.click_relative(61, 22)
                self.type_keys_with_interval(1,'0081260')
                self.enter()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                self.tab()
                if not self.find( "b_servico_genq", matching=0.97, waiting_time=10000):
                    self.not_found("b_servico_genq")
                self.click_relative(65, 22)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                self.tab()
                x=0
                while x<4:
                    if not self.find( "loop_origemmovimento_genq", matching=0.97, waiting_time=10000):
                        self.not_found("loop_origemmovimento_genq")
                    self.click_relative(171, 24)
                    self.type_down()
                    self.enter()
                    x=x+1
                x=0
                while x<4:
                    if not self.find( "loop_origemmovimento_genq", matching=0.97, waiting_time=10000):
                        self.not_found("loop_origemmovimento_genq")
                    self.click_relative(171, 24)
                    self.type_up()
                    self.enter()
                    x=x+1
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()         
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                                ####---GESTAO DOC E---####
                                
                if not self.find( "vendas2", matching=0.97, waiting_time=10000):
                    self.not_found("vendas2")
                self.click()
                if not self.find( "gestaodoce", matching=0.97, waiting_time=10000):
                    self.not_found("gestaodoce")
                self.click()
                if not self.find( "loop_doce_gd", matching=0.97, waiting_time=10000):
                    self.not_found("loop_doce_gd")
                self.click_relative(750, 86)
                x=0
                while x<7:
                    self.type_down()
                    self.space()
                    x=x+1
                x=0
                while x<7:
                    self.type_up()
                    self.space()
                    x=x+1
                self.type_down()
                self.type_down()
                self.space()
                self.type_up()
                self.space()
                if not self.find( "loop_situacao_gdc", matching=0.97, waiting_time=10000):
                    self.not_found("loop_situacao_gdc")
                self.click_relative(113, 23)
                x=0
                while x<19:
                    self.type_down()
                    self.space()
                    x=x+1
                self.tab()
                self.type_down()
                self.type_down()
                self.type_down()
                if not self.find( "periodo_gdc", matching=0.97, waiting_time=10000):
                    self.not_found("periodo_gdc")
                self.click_relative(389, 84)
                if not self.find( "periodo_ano", matching=0.97, waiting_time=10000):
                    self.not_found("periodo_ano")
                self.click()
                if not self.find( "periodo_ano_atual", matching=0.97, waiting_time=10000):
                    self.not_found("periodo_ano_atual")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                self.wait(1000)
                if not self.find( "seleciona_gestaodoce", matching=0.97, waiting_time=10000):
                    self.not_found("seleciona_gestaodoce")
                self.click_relative(36, 23)
                if not self.find( "inutilizar_gdc", matching=0.97, waiting_time=10000):
                    self.not_found("inutilizar_gdc")
                self.click_relative(81, -1)
                if not self.find( "documentosselecionados", matching=0.97, waiting_time=10000):
                    self.not_found("documentosselecionados")
                self.click()
                self.type_keys_with_interval(1,'feito por teste automatico')
                self.enter()
                self.enter()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "fechargestaoadm", matching=0.97, waiting_time=10000):
                    self.not_found("fechargestaoadm")
                self.click()
                self.enter()
                #if not self.find( "fechargestaoadm", matching=0.97, waiting_time=10000):
                #    self.not_found("fechargestaoadm")
                #self.click()
                if not self.find( "simfecharfim", matching=0.97, waiting_time=10000):
                    self.not_found("simfecharfim")
                self.click()
                #self.enter()

                        #SESSÃO PÁGINA 8 (Manutenções 20482 - 23925)

                #######################-----LOGIN-----############################
            
                #self.execute(r"C:\Users\Rafael\Desktop\2207\bug\faturamento.exe")
                self.execute(r"C:\Users\Rafael\Desktop\2207\teste23\23mes07\faturamento.exe")
                
                if not self.find( "btn_codigo_usuario", matching=0.97, waiting_time=1000000):
                    self.not_found("btn_codigo_usuario")
                self.click_relative(47, 12)
                        
                self.type_keys_with_interval(1,"999")
                self.wait(500)
                self.type_keys_with_interval(1,"tsfmx24")
                self.enter()

                if not self.find( "btn_login", matching=0.97, waiting_time=10000):
                    self.not_found("btn_login")
                self.click()
                self.enter()    
                

                ###################################################################
                
                self.wait(1500)
                if not self.find( "manutencoes2.0", matching=0.97, waiting_time=100000):
                    self.not_found("manutencoes2.0")
                self.click()
                self.wait(1500)
                self.type_down()
                #if not self.find( "manut_clientesfornecedores2.0", matching=0.97, waiting_time=10000):
                #    self.not_found("manut_clientesfornecedores2.0")
                #self.click()
                self.wait(1500)
                self.enter()         
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                self.wait(3000)
                self.enter()
                if not self.find( "incluirregistro_manut", matching=0.97, waiting_time=10000):
                    self.not_found("incluirregistro_manut")
                self.click()
                self.enter()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "alterar_manut", matching=0.97, waiting_time=10000):
                    self.not_found("alterar_manut")
                self.click()
                if not self.find( "b_contabilfixo_manut", matching=0.97, waiting_time=10000):
                    self.not_found("b_contabilfixo_manut")
                self.click_relative(82, 26)
                self.tab()
                self.tab()
                self.tab()
                self.type_down()
                self.type_down()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "b_contabilfornecedor_manut", matching=0.97, waiting_time=10000):
                    self.not_found("b_contabilfornecedor_manut")
                self.click_relative(78, 25)
                self.tab()
                self.tab()
                self.tab()
                self.type_down()
                self.type_down()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "b_transportador_manut", matching=0.97, waiting_time=10000):
                    self.not_found("b_transportador_manut")
                self.click_relative(79, 24)
                self.type_keys_with_interval(1,'0081260')
                self.enter()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "b_condpag_manut", matching=0.97, waiting_time=10000):
                    self.not_found("b_condpag_manut")
                self.click_relative(79, 25)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "aba2_manutclientes", matching=0.97, waiting_time=10000):
                    self.not_found("aba2_manutclientes")
                self.click()
                if not self.find( "b_vendedorcomprador_manutclientes", matching=0.97, waiting_time=10000):
                    self.not_found("b_vendedorcomprador_manutclientes")
                self.click_relative(61, 39)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                self.tab()
                if not self.find( "b_localcobranca_manutcliente", matching=0.97, waiting_time=10000):
                    self.not_found("b_localcobranca_manutcliente")
                self.click_relative(62, 84)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                self.tab()
                if not self.find( "b_classificacao_manutcliente", matching=0.97, waiting_time=10000):
                    self.not_found("b_classificacao_manutcliente")
                self.click_relative(62, 126)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                self.tab()
                if not self.find( "b_regiao_manutcliente", matching=0.97, waiting_time=10000):
                    self.not_found("b_regiao_manutcliente")
                self.click_relative(289, 42)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                self.tab()
                if not self.find( "b_ramoatividade_manutcliente", matching=0.97, waiting_time=10000):
                    self.not_found("b_ramoatividade_manutcliente")
                self.click_relative(288, 82)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                self.tab()
                if not self.find( "b_operacao_manutcliente", matching=0.97, waiting_time=10000):
                    self.not_found("b_operacao_manutcliente")
                self.click_relative(285, 126)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                self.tab()
                if not self.find( "b_estado_manutcliente", matching=0.97, waiting_time=10000):
                    self.not_found("b_estado_manutcliente")
                self.click_relative(513, 41)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                self.tab()
                if not self.find( "b_segmento_manutcliente", matching=0.97, waiting_time=10000):
                    self.not_found("b_segmento_manutcliente")
                self.click_relative(512, 84)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                self.tab()
                if not self.find( "b_municipio_manutcliente", matching=0.97, waiting_time=10000):
                    self.not_found("b_municipio_manutcliente")
                self.click_relative(739, 39)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                self.tab()
                if not self.find( "b_linha_manutcliente", matching=0.97, waiting_time=10000):
                    self.not_found("b_linha_manutcliente")
                self.click_relative(741, 80)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.enter()
                if not self.find( "b_vendaux_manutcliente", matching=0.97, waiting_time=10000):
                    self.not_found("b_vendaux_manutcliente")
                self.click_relative(965, 41)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                self.tab()
                if not self.find( "b_comissao_manutcliente", matching=0.97, waiting_time=10000):
                    self.not_found("b_comissao_manutcliente")
                self.click_relative(967, 83)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                self.tab()
                if not self.find( "b_tabpreco_manutcliente", matching=0.97, waiting_time=10000):
                    self.not_found("b_tabpreco_manutcliente")
                self.click_relative(947, 128)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                self.tab()
                if not self.find( "b_rota_manutcliente", matching=0.97, waiting_time=10000):
                    self.not_found("b_rota_manutcliente")
                self.click_relative(1236, 42)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                self.tab()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                self.wait(3000)
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                                ####---CONTRATOS CLIENTES/FORNECEDORES---####
                                
                if not self.find( "manutencoes2.0", matching=0.97, waiting_time=10000):
                    self.not_found("manutencoes2.0")
                self.click()
                if not self.find( "contratosdeclientesfornecedores", matching=0.97, waiting_time=10000):
                    self.not_found("contratosdeclientesfornecedores")
                self.click()
                if not self.find( "incluirregistro_manut", matching=0.97, waiting_time=10000):
                    self.not_found("incluirregistro_manut")
                self.click()
                #self.type_keys_with_interval(1,'0081260')
                self.enter()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "alterar_manut", matching=0.97, waiting_time=10000):
                    self.not_found("alterar_manut")
                self.click()
                if not self.find( "b_tipocontrato_manutCC", matching=0.97, waiting_time=10000):
                    self.not_found("b_tipocontrato_manutCC")
                self.click_relative(61, 41)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.enter()
                if not self.find( "b_comissao_manutCC", matching=0.97, waiting_time=10000):
                    self.not_found("b_comissao_manutCC")
                self.click_relative(464, 43)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "retornar_alteradados_manutcc", matching=0.97, waiting_time=10000):
                    self.not_found("retornar_alteradados_manutcc")
                self.click_relative(40, 42)            
                if not self.find( "aba2_manutclientes", matching=0.97, waiting_time=10000):
                    self.not_found("aba2_manutclientes")
                self.click()
                if not self.find( "b_mcc_vendedorcomprador", matching=0.97, waiting_time=10000):
                    self.not_found("b_mcc_vendedorcomprador")
                self.click_relative(66, 42)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                self.tab()
                if not self.find( "b_mcc_rota", matching=0.97, waiting_time=10000):
                    self.not_found("b_mcc_rota")
                self.click_relative(64, 83)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                self.tab()
                if not self.find( "b_mcc_linha", matching=0.97, waiting_time=10000):
                    self.not_found("b_mcc_linha")
                self.click_relative(64, 125)
                if not self.find( "retornar_consultalinhas", matching=0.97, waiting_time=10000):
                    self.not_found("retornar_consultalinhas")
                self.click_relative(33, 47)
                if not self.find( "b_mcc_regiao", matching=0.97, waiting_time=10000):
                    self.not_found("b_mcc_regiao")
                self.click_relative(394, 43)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                self.tab()
                if not self.find( "b_mcc_localdecobranca", matching=0.97, waiting_time=10000):
                    self.not_found("b_mcc_localdecobranca")
                self.click_relative(396, 84)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                self.tab()
                if not self.find( "b_mcc_comissao", matching=0.97, waiting_time=10000):
                    self.not_found("b_mcc_comissao")
                self.click_relative(394, 126)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                self.tab()
                if not self.find( "b_mcc_estado", matching=0.97, waiting_time=10000):
                    self.not_found("b_mcc_estado")
                self.click_relative(726, 41)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                self.tab()
                if not self.find( "b_mcc_ramoatividade", matching=0.97, waiting_time=10000):
                    self.not_found("b_mcc_ramoatividade")
                self.click_relative(725, 85)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                self.tab()
                if not self.find( "b_mcc_classificacao", matching=0.97, waiting_time=10000):
                    self.not_found("b_mcc_classificacao")
                self.click_relative(721, 121)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                self.tab()
                if not self.find( "b_mcc_municipio", matching=0.97, waiting_time=10000):
                    self.not_found("b_mcc_municipio")
                self.click_relative(1056, 42)
                self.tab()
                self.tab()
                self.tab()
                self.type_down()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                self.tab()
                if not self.find( "b_mcc_segmento", matching=0.97, waiting_time=10000):
                    self.not_found("b_mcc_segmento")
                self.click_relative(1055, 81)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                self.tab()
                if not self.find( "b_mcc_tipocontrato", matching=0.97, waiting_time=10000):
                    self.not_found("b_mcc_tipocontrato")
                self.click_relative(1057, 126)
                self.tab()
                self.tab()
                self.space()
                self.space()
                self.tab()
                self.type_keys_with_interval(1,'123')
                self.tab()
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=0
                while x<3:
                    self.type_down()
                    x=x+1
                x=0
                while x<3:
                    self.type_up()
                    x=x+1
                self.tab()
                x=0
                while x<13:
                    self.type_down()
                    x=x+1
                x=0
                while x<13:
                    self.type_up()
                    x=x+1
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                x=0
                while x<6:
                    self.backspace()
                    x=x+1
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                x=0
                while x<6:
                    self.backspace()
                    x=x+1
                self.tab()
                self.tab()
                self.tab()
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                x=0
                while x<6:
                    self.backspace()
                    x=x+1
                self.tab()
                self.space()
                self.space()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                self.enter()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                                ####---MANUTENCAO ITENS---####
                                
                if not self.find( "manutencoes2.0", matching=0.97, waiting_time=10000):
                    self.not_found("manutencoes2.0")
                self.click()
                if not self.find( "manutencao_itens", matching=0.97, waiting_time=10000):
                    self.not_found("manutencao_itens")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                self.wait(3000)
                if not self.find( "alterar_manut", matching=0.97, waiting_time=10000):
                    self.not_found("alterar_manut")
                self.click()
                if not self.find( "b_ncm_MI", matching=0.97, waiting_time=10000):
                    self.not_found("b_ncm_MI")
                self.click_relative(170, 64)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "b_familia_MI", matching=0.97, waiting_time=10000):
                    self.not_found("b_familia_MI")
                self.click_relative(52, 46)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "b_marca_MI", matching=0.97, waiting_time=10000):
                    self.not_found("b_marca_MI")
                self.click_relative(54, 91)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "b_controle_MI", matching=0.97, waiting_time=10000):
                    self.not_found("b_controle_MI")
                self.click_relative(53, 127)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "b_unidadeestoque_MI", matching=0.97, waiting_time=10000):
                    self.not_found("b_unidadeestoque_MI")
                self.click_relative(55, 171)
                self.tab()
                self.tab()
                self.tab()
                self.type_down()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "b_99997_MI", matching=0.97, waiting_time=10000):
                    self.not_found("b_99997_MI")
                self.click_relative(53, 213)
                self.tab()
                self.tab()
                self.tab()
                self.type_down()
                self.type_down()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "b_grupo_MI", matching=0.97, waiting_time=10000):
                    self.not_found("b_grupo_MI")
                self.click_relative(385, 43)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "b_tipo_MI", matching=0.97, waiting_time=10000):
                    self.not_found("b_tipo_MI")
                self.click_relative(385, 90)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "b_centrocusto_MI", matching=0.97, waiting_time=10000):
                    self.not_found("b_centrocusto_MI")
                self.click_relative(419, 128)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "b_grupofiscal_MI", matching=0.97, waiting_time=10000):
                    self.not_found("b_grupofiscal_MI")
                self.click_relative(388, 171)
                self.tab()
                self.tab()
                self.tab()
                self.type_down()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "b_99980_MI", matching=0.97, waiting_time=10000):
                    self.not_found("b_99980_MI")
                self.click_relative(386, 213)
                self.tab()
                self.tab()
                self.tab()
                self.type_down()
                self.type_down()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "b_subgrupos_MI", matching=0.97, waiting_time=10000):
                    self.not_found("b_subgrupos_MI")
                self.click_relative(717, 47)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "b_subtipos_MI", matching=0.97, waiting_time=10000):
                    self.not_found("b_subtipos_MI")
                self.click_relative(716, 89)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "b_cadeiapreco_MI", matching=0.97, waiting_time=10000):
                    self.not_found("b_cadeiapreco_MI")
                self.click_relative(720, 130)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "b_genA_MI", matching=0.97, waiting_time=10000):
                    self.not_found("b_genA_MI")
                self.click_relative(717, 173)
                if not self.find( "retornar_generico", matching=0.97, waiting_time=10000):
                    self.not_found("retornar_generico")
                self.click_relative(36, 34)
                if not self.find( "b_genB_MI", matching=0.97, waiting_time=10000):
                    self.not_found("b_genB_MI")
                self.click_relative(720, 215)
                if not self.find( "retornar_generico", matching=0.97, waiting_time=10000):
                    self.not_found("retornar_generico")
                self.click_relative(36, 34)
                if not self.find( "b_fornecedoritem_MI", matching=0.97, waiting_time=10000):
                    self.not_found("b_fornecedoritem_MI")
                self.click_relative(62, 24)
                self.wait(500)
                self.type_keys_with_interval(1,'0081260')
                self.enter()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                x=0
                while x<13:
                    self.tab()
                    x=x+1
                x=0
                while x<10:
                    self.type_down()
                    x=x+1
                x=0
                while x<10:
                    self.type_up()
                    x=x+1
                self.tab()
                self.tab()
                self.tab()
                x=0
                while x<8:
                    self.type_down()
                    x=x+1
                x=0
                while x<8:
                    self.type_up()
                    x=x+1
                x=0
                while x<4:
                    self.tab()
                    x=x+1
                x=0
                while x<13:
                    self.type_down()
                    x=x+1
                x=0
                while x<13:
                    self.type_up()
                    x=x+1
                self.tab()
                x=0
                while x<4:
                    self.type_down()
                    x=x+1
                self.tab()
                self.tab()
                x=0
                while x<3:
                    self.type_down()
                    x=x+1
                x=0
                while x<3:
                    self.type_up()
                    x=x+1
                self.tab()
                x=0
                while x<3:
                    self.type_down()
                    x=x+1
                x=0
                while x<3:
                    self.type_up()
                    x=x+1
                if not self.find( "retornar_alteradados_manutcc", matching=0.97, waiting_time=10000):
                    self.not_found("retornar_alteradados_manutcc")
                self.click_relative(40, 42)                  
                if not self.find( "aba2_manutclientes", matching=0.97, waiting_time=10000):
                    self.not_found("aba2_manutclientes")
                self.click()
                if not self.find( "b_itemcomp_manutI", matching=0.97, waiting_time=10000):
                    self.not_found("b_itemcomp_manutI")
                self.click_relative(55, 108)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "d_periodo1_manutI", matching=0.97, waiting_time=10000):
                    self.not_found("d_periodo1_manutI")
                self.click_relative(695, 111)
                if not self.find( "CA_periodo", matching=0.97, waiting_time=10000):
                    self.not_found("CA_periodo")
                self.click()
                if not self.find( "CA_periodo_atual", matching=0.97, waiting_time=10000):
                    self.not_found("CA_periodo_atual")
                self.click()
                if not self.find( "d_periodo2_manutI", matching=0.97, waiting_time=10000):
                    self.not_found("d_periodo2_manutI")
                self.click_relative(931, 110)
                if not self.find( "CA_periodo", matching=0.97, waiting_time=10000):
                    self.not_found("CA_periodo")
                self.click()
                if not self.find( "CA_periodo_atual", matching=0.97, waiting_time=10000):
                    self.not_found("CA_periodo_atual")
                self.click()
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "d_periodo3_manutI", matching=0.97, waiting_time=10000):
                    self.not_found("d_periodo3_manutI")
                self.click_relative(1278, 109)
                if not self.find( "CA_periodo", matching=0.97, waiting_time=10000):
                    self.not_found("CA_periodo")
                self.click()
                if not self.find( "CA_periodo_atual", matching=0.97, waiting_time=10000):
                    self.not_found("CA_periodo_atual")
                self.click()
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "pesaveis_sim", matching=0.97, waiting_time=10000):
                    self.not_found("pesaveis_sim")
                self.click_relative(10, 29)
                if not self.find( "pesaveis_nao", matching=0.97, waiting_time=10000):
                    self.not_found("pesaveis_nao")
                self.click_relative(95, 30)
                if not self.find( "pesaveis_todos", matching=0.97, waiting_time=10000):
                    self.not_found("pesaveis_todos")
                self.click_relative(159, 29)
                if not self.find( "nme_sim", matching=0.97, waiting_time=10000):
                    self.not_found("nme_sim")
                self.click_relative(9, 29)
                if not self.find( "nme_nao", matching=0.97, waiting_time=10000):
                    self.not_found("nme_nao")
                self.click_relative(87, 28)
                if not self.find( "nme_todos", matching=0.97, waiting_time=10000):
                    self.not_found("nme_todos")
                self.click_relative(161, 31)
                if not self.find( "ie_sim", matching=0.97, waiting_time=10000):
                    self.not_found("ie_sim")
                self.click_relative(8, 29)
                if not self.find( "ie_nao", matching=0.97, waiting_time=10000):
                    self.not_found("ie_nao")
                self.click_relative(83, 29)
                if not self.find( "ie_todos", matching=0.97, waiting_time=10000):
                    self.not_found("ie_todos")
                self.click_relative(159, 27)
                if not self.find( "vnfe_sim", matching=0.97, waiting_time=10000):
                    self.not_found("vnfe_sim")
                self.click_relative(9, 29)
                if not self.find( "vnfe_nao", matching=0.97, waiting_time=10000):
                    self.not_found("vnfe_nao")
                self.click_relative(84, 30)
                if not self.find( "vnfe_todos", matching=0.97, waiting_time=10000):
                    self.not_found("vnfe_todos")
                self.click_relative(158, 30)
                if not self.find( "nfrac_sim", matching=0.97, waiting_time=10000):
                    self.not_found("nfrac_sim")
                self.click_relative(9, 29)
                if not self.find( "nfrac_nao", matching=0.97, waiting_time=10000):
                    self.not_found("nfrac_nao")
                self.click_relative(83, 30)
                if not self.find( "nfrac_todos", matching=0.97, waiting_time=10000):
                    self.not_found("nfrac_todos")
                self.click_relative(158, 29)
                self.tab()
                x=0
                while x<3:
                    self.type_down()
                    x=x+1
                x=0
                while x<3:
                    self.type_up()
                    x=x+1
                self.tab()
                x=0
                while x<2:
                    self.type_down()
                    x=x+1
                x=0
                while x<2:
                    self.type_up()
                    x=x+1
                self.tab()
                x=0
                while x<9:
                    self.type_down()
                    x=x+1
                x=0
                while x<9:
                    self.type_up()
                    x=x+1
                x=0
                while x<7:
                    self.tab()
                    self.space()
                    self.space()
                    x=x+1
                self.tab()
                x=0
                while x<4:
                    self.tab()
                    self.space()
                    self.space()
                    x=x+1
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                                ####---ITENS COMPOSICAO---####
                                
                if not self.find( "manutencoes2.0", matching=0.97, waiting_time=10000):
                    self.not_found("manutencoes2.0")
                self.click()
                if not self.find( "itenscomposicao", matching=0.97, waiting_time=10000):
                    self.not_found("itenscomposicao")
                self.click()
                if not self.find( "b_composto_manutIC", matching=0.97, waiting_time=10000):
                    self.not_found("b_composto_manutIC")
                self.click_relative(126, 82)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                if not self.find( "b_substituto_manutIC", matching=0.97, waiting_time=10000):
                    self.not_found("b_substituto_manutIC")
                self.click_relative(125, 103)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                self.tab()
                self.tab()
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=0
                while x<3:
                    self.type_down()
                    x=x+1
                x=0
                while x<3:
                    self.type_up()
                    x=x+1
                if not self.find( "ir_manutIC", matching=0.97, waiting_time=10000):
                    self.not_found("ir_manutIC")
                self.click_relative(15, 180)
                if not self.find( "buscaritensreqcompras", matching=0.97, waiting_time=10000):
                    self.not_found("buscaritensreqcompras")
                self.click_relative(10, 31)
                self.type_keys_with_interval(1,'agulha gengival')
                self.enter()
                self.type_down()
                self.type_down()
                self.type_down()
                self.type_down()
                self.wait(500)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # self.wait(500)
                # if not self.find( "quantidade_lancitens", matching=0.97, waiting_time=10000):
                #     self.not_found("quantidade_lancitens")
                # self.click_relative(336, 280)
                # self.backspace()
                # self.enter()
                # x=0
                # while x<31:
                #     self.type_down()
                #     x=x+1
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # self.wait(500)
                
                self.type_keys_with_interval(1,'1')
                if not self.find( "botaoconfirmaritensreqcompras", matching=0.97, waiting_time=10000):
                    self.not_found("botaoconfirmaritensreqcompras")
                self.click()
                self.wait(3000)
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                self.wait(3000)
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                self.enter()
                
                                ####---PRECOS E CUSTOS---####
                                
                if not self.find( "manutencoes2.0", matching=0.97, waiting_time=10000):
                    self.not_found("manutencoes2.0")
                self.click()
                if not self.find( "precosecustos", matching=0.97, waiting_time=10000):
                    self.not_found("precosecustos")
                self.click()
                if not self.find( "aba2_manutclientes", matching=0.97, waiting_time=10000):
                    self.not_found("aba2_manutclientes")
                self.click()
                if not self.find( "b_tabelapreco_manutP", matching=0.97, waiting_time=10000):
                    self.not_found("b_tabelapreco_manutP")
                self.click_relative(63, 23)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.enter()
                self.tab()
                self.tab()
                self.tab()
                self.tab()
                self.tab()
                self.tab()
                x=0
                while x<9:
                    self.type_down()
                    x=x+1
                x=0
                while x<9:
                    self.type_up()
                    x=x+1
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                self.wait(3000)
                if not self.find( "alteracoes_manut", matching=0.97, waiting_time=10000):
                    self.not_found("alteracoes_manut")
                self.click()
                if not self.find( "a_geralcomformula", matching=0.97, waiting_time=10000):
                    self.not_found("a_geralcomformula")
                self.click()
                if not self.find( "retorna_p1_manut", matching=0.97, waiting_time=10000):
                    self.not_found("retorna_p1_manut")
                self.click_relative(51, 39)
                if not self.find( "alteracoes_manut", matching=0.97, waiting_time=10000):
                    self.not_found("alteracoes_manut")
                self.click()
                
                # if not self.find( "a_individualcomformula", matching=0.97, waiting_time=10000):
                #     self.not_found("a_individualcomformula")
                # self.click()
                # if not self.find( "b_operacao_p2manut", matching=0.97, waiting_time=10000):
                #     self.not_found("b_operacao_p2manut")
                # self.click_relative(65, 194)
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # self.wait(500)
                # if not self.find( "b_regiao_p2manut", matching=0.97, waiting_time=10000):
                #     self.not_found("b_regiao_p2manut")
                # self.click_relative(430, 199)
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # self.wait(500)
                # if not self.find( "retornar_p2manut", matching=0.97, waiting_time=10000):
                #     self.not_found("retornar_p2manut")
                # self.click_relative(24, 39)
                # self.type_right()
                # self.enter()
                
                # if not self.find( "alteracoes_manut", matching=0.97, waiting_time=10000):
                #     self.not_found("alteracoes_manut")
                # self.click()
                
                if not self.find( "a_p3geral_manut", matching=0.97, waiting_time=10000):
                    self.not_found("a_p3geral_manut")
                self.click()
                if not self.find( "retornar_manut_geral", matching=0.97, waiting_time=10000):
                    self.not_found("retornar_manut_geral")
                self.click_relative(39, 39)
                if not self.find( "alteracoes_manut", matching=0.97, waiting_time=10000):
                    self.not_found("alteracoes_manut")
                self.click()
                if not self.find( "a_individual_p4manut", matching=0.97, waiting_time=10000):
                    self.not_found("a_individual_p4manut")
                self.click()
                if not self.find( "b_item_p4manut", matching=0.97, waiting_time=10000):
                    self.not_found("b_item_p4manut")
                self.click_relative(160, 110)
                self.wait(500)
                if not self.find( "b_item_p4manut", matching=0.97, waiting_time=10000):
                    self.not_found("b_item_p4manut")
                self.click_relative(160, 110)
                self.enter()
                x=0
                while x<31:
                    self.type_down()
                    x=x+1
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "retornar_p4manut", matching=0.97, waiting_time=10000):
                    self.not_found("retornar_p4manut")
                self.click_relative(36, 35)
                if not self.find( "alteracoes_manut", matching=0.97, waiting_time=10000):
                    self.not_found("alteracoes_manut")
                self.click()
                if not self.find( "a_p5manut", matching=0.97, waiting_time=10000):
                    self.not_found("a_p5manut")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "alteracoes_manut", matching=0.97, waiting_time=10000):
                    self.not_found("alteracoes_manut")
                self.click()
                if not self.find( "a_p6manut", matching=0.97, waiting_time=10000):
                    self.not_found("a_p6manut")
                self.click()
                self.wait(10000)
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                self.enter()
                self.enter()
                self.wait(1000)

                                ####---OFERTAS---####
                                
                if not self.find( "manutencoes2.0", matching=0.97, waiting_time=10000):
                    self.not_found("manutencoes2.0")
                self.click()
                self.wait(1000)
                if not self.find( "ofertas", matching=0.97, waiting_time=10000):
                    self.not_found("ofertas")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                                ####---SERVIÇOS---####
                
                if not self.find( "manutencoes2.0", matching=0.97, waiting_time=10000):
                    self.not_found("manutencoes2.0")
                self.click()
                if not self.find( "manutservicos", matching=0.97, waiting_time=10000):
                    self.not_found("manutservicos")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "aba2_manutclientes", matching=0.97, waiting_time=10000):
                    self.not_found("aba2_manutclientes")
                self.click()
                if not self.find( "b_tabpreco_manutserv", matching=0.97, waiting_time=10000):
                    self.not_found("b_tabpreco_manutserv")
                self.click_relative(55, 199)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.enter()
                
                # if not self.find( "alterar_manut", matching=0.97, waiting_time=10000):
                #     self.not_found("alterar_manut")
                # self.click()
                # if not self.find( "b_familia_mserv", matching=0.97, waiting_time=10000):
                #     self.not_found("b_familia_mserv")
                # self.click_relative(52, 170)
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # if not self.find( "b_marca_mserv", matching=0.97, waiting_time=10000):
                #     self.not_found("b_marca_mserv")
                # self.click_relative(54, 211)
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # if not self.find( "b_uniest_mserv", matching=0.97, waiting_time=10000):
                #     self.not_found("b_uniest_mserv")
                # self.click_relative(54, 251)
                # self.tab()
                # self.tab()
                # self.tab()
                # self.type_down()
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # if not self.find( "b_grupo_mserv", matching=0.97, waiting_time=10000):
                #     self.not_found("b_grupo_mserv")
                # self.click_relative(386, 170)
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # if not self.find( "b_grupofiscal_mserv", matching=0.97, waiting_time=10000):
                #     self.not_found("b_grupofiscal_mserv")
                # self.click_relative(385, 210)
                # self.tab()
                # self.tab()
                # self.tab()
                # self.type_down()
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # self.wait(500)
                # if not self.find( "b_subgrupo_mserv", matching=0.97, waiting_time=10000):
                #     self.not_found("b_subgrupo_mserv")
                # self.click_relative(721, 169)
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # self.wait(500)
                # if not self.find( "b_planodecontas_mserv", matching=0.97, waiting_time=10000):
                #     self.not_found("b_planodecontas_mserv")
                # self.click_relative(718, 211)
                # self.tab()
                # self.tab()
                # self.tab()
                # self.type_down()
                # self.type_down()
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # self.wait(500)
                # if not self.find( "b_alteradados_mserv", matching=0.97, waiting_time=10000):
                #     self.not_found("b_alteradados_mserv")
                # self.click_relative(39, 40)
                
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                                ####---SERVICOS PRECOS---####
                                
                if not self.find( "manutencoes2.0", matching=0.97, waiting_time=10000):
                    self.not_found("manutencoes2.0")
                self.click()
                if not self.find( "servicoprecos", matching=0.97, waiting_time=10000):
                    self.not_found("servicoprecos")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "alteracoes_manut", matching=0.97, waiting_time=10000):
                    self.not_found("alteracoes_manut")
                self.click()
                if not self.find( "alteracoesprecotabela", matching=0.97, waiting_time=10000):
                    self.not_found("alteracoesprecotabela")
                self.click()
                self.type_left()
                self.enter()
                if not self.find( "alteracoes_manut", matching=0.97, waiting_time=10000):
                    self.not_found("alteracoes_manut")
                self.click()
                if not self.find( "alteracoesprecotabela", matching=0.97, waiting_time=10000):
                    self.not_found("alteracoesprecotabela")
                self.click()
                self.type_left()
                self.type_left()
                self.enter()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                self.enter()
                
                                ####---NCM---####
                                
                if not self.find( "manutencoes2.0", matching=0.97, waiting_time=10000):
                    self.not_found("manutencoes2.0")
                self.click()
                if not self.find( "NCMmanut", matching=0.97, waiting_time=10000):
                    self.not_found("NCMmanut")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "alterar_manut", matching=0.97, waiting_time=10000):
                    self.not_found("alterar_manut")
                self.click()
                if not self.find( "retornar_altera_NCM", matching=0.97, waiting_time=10000):
                    self.not_found("retornar_altera_NCM")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                                ####---ESTADOS NCM---####
                                
                if not self.find( "manutencoes2.0", matching=0.97, waiting_time=10000):
                    self.not_found("manutencoes2.0")
                self.click()
                if not self.find( "esstadosNCM_manut", matching=0.97, waiting_time=10000):
                    self.not_found("esstadosNCM_manut")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "alterar_manut", matching=0.97, waiting_time=10000):
                    self.not_found("alterar_manut")
                self.click()
                self.tab()
                self.tab()
                x=0
                while x<10:
                    self.type_keys_with_interval(1,'123')
                    self.tab()
                    x=x+1
                if not self.find( "retorna_dadosENCM", matching=0.97, waiting_time=10000):
                    self.not_found("retorna_dadosENCM")
                self.click_relative(43, 44) 
                if not self.find( "addregistro_manutecnm", matching=0.97, waiting_time=10000):
                    self.not_found("addregistro_manutecnm")
                self.click()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.enter()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                                ####---MANUT CONDICAO PAGAMENTO---####
                
                if not self.find( "manutencoes2.0", matching=0.97, waiting_time=10000):
                    self.not_found("manutencoes2.0")
                self.click()
                if not self.find( "manutcondpagamento", matching=0.97, waiting_time=10000):
                    self.not_found("manutcondpagamento")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "alterar_manut", matching=0.97, waiting_time=10000):
                    self.not_found("alterar_manut")
                self.click()
                
                                ####---RECALCULO CUSTO MEDIO MERCANTIL---####
                                
                if not self.find( "manutencoes2.0", matching=0.97, waiting_time=10000):
                    self.not_found("manutencoes2.0")
                self.click()
                if not self.find( "recalculocustomediomercantilmanut", matching=0.97, waiting_time=10000):
                    self.not_found("recalculocustomediomercantilmanut")
                self.click()
                if not self.find( "aba2_recalculocustomedio_manut", matching=0.97, waiting_time=10000):
                    self.not_found("aba2_recalculocustomedio_manut")
                self.click()
                
                if not self.find( "b_item_manutRCmedio", matching=0.97, waiting_time=10000):
                    self.not_found("b_item_manutRCmedio")
                self.click_relative(72, 169)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                self.wait(2000)
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.type_keys_with_interval(1,'123')
                self.tab()
                self.type_keys_with_interval(1,'123')
                if not self.find( "b_operacao_RCmedio", matching=0.97, waiting_time=10000):
                    self.not_found("b_operacao_RCmedio")
                self.click_relative(65, 191)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.tab()
                self.tab()
                self.type_up()
                x=0
                while x<3:
                    self.type_down()
                    x=x+1
                x=0
                while x<3:
                    self.type_up()
                    x=x+1
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.type_keys_with_interval(1,'123')
                self.tab()
                self.type_keys_with_interval(1,'123')
                self.tab()
                self.tab()
                self.tab()
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "addregistro_manutecnm", matching=0.97, waiting_time=10000):
                    self.not_found("addregistro_manutecnm")
                self.click()
                if not self.find( "b_lancitens_manut", matching=0.97, waiting_time=10000):
                    self.not_found("b_lancitens_manut")
                self.click_relative(14, 34)
                self.type_keys_with_interval(1,'agulha gengival')
                self.enter()
                self.type_down()
                self.type_down()
                self.type_down()
                self.type_down()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(2000)
                self.type_keys_with_interval(1,'1')
                self.tab()
                self.tab()
                self.tab()
                self.tab()
                self.tab()
                self.enter()
                self.wait(1000)
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                    self.not_found("salvarrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                self.backspace()
                self.tab()
                if not self.find( "p_reccustomedio", matching=0.97, waiting_time=10000):
                    self.not_found("p_reccustomedio")
                self.click_relative(230, 88)            
                if not self.find( "CA_periodo", matching=0.97, waiting_time=10000):
                    self.not_found("CA_periodo")
                self.click()
                if not self.find( "CA_periodo_atual", matching=0.97, waiting_time=10000):
                    self.not_found("CA_periodo_atual")
                self.click()
                # 
                # if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                #     self.not_found("localizarfim")
                # self.click()
                # self.enter()
                # if not self.find( "s_codteste_recmedio", matching=0.97, waiting_time=10000):
                #     self.not_found("s_codteste_recmedio")
                # self.click()
                # if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                #     self.not_found("editarfim")
                # self.click()
                # if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                #     self.not_found("excluirrs")
                # self.click()
                # if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                #     self.not_found("simexcluirrs")
                # self.click()
                # if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                #     self.not_found("retornarfim")
                # self.click()
                # if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                #     self.not_found("localizarfim")
                # self.click()
                # 
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                                ####---MANUT MOV FRETES---####
                                
                if not self.find( "manutencoes2.0", matching=0.97, waiting_time=10000):
                    self.not_found("manutencoes2.0")
                self.click()
                if not self.find( "manutmovfretes_aba", matching=0.97, waiting_time=10000):
                    self.not_found("manutmovfretes_aba")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()                 
                if not self.find( "alterar_manut", matching=0.97, waiting_time=10000):
                    self.not_found("alterar_manut")
                self.click()
                if not self.find( "b_operacao_alteradados_manutfrete", matching=0.97, waiting_time=10000):
                    self.not_found("b_operacao_alteradados_manutfrete")
                self.click_relative(71, 111)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "b_cfop_alteradados_manutfrete", matching=0.97, waiting_time=10000):
                    self.not_found("b_cfop_alteradados_manutfrete")
                self.click_relative(465, 111)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "retornar_alteradados_manutfrete", matching=0.97, waiting_time=10000):
                    self.not_found("retornar_alteradados_manutfrete")
                self.click_relative(44, 41)
                if not self.find( "b_transportador_manutfrete", matching=0.97, waiting_time=10000):
                    self.not_found("b_transportador_manutfrete")
                self.click_relative(421, 85)
                self.type_keys_with_interval(1,'0081260')
                self.enter()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                                ####---ESTOQUE---####
                                
                if not self.find( "estoque4.1", matching=0.97, waiting_time=10000):
                    self.not_found("estoque4.1")
                self.click()   
                self.type_down()                     
                self.enter()                      
                self.wait(1500)
                self.enter()
                if not self.find( "aba2_estoque_entradasaidaserv", matching=0.97, waiting_time=10000):
                    self.not_found("aba2_estoque_entradasaidaserv")
                self.click()
                if not self.find( "b_codop_meserv", matching=0.97, waiting_time=10000):
                    self.not_found("b_codop_meserv")
                self.click_relative(74, 321)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                if not self.find( "b_condpag_mserv", matching=0.97, waiting_time=10000):
                    self.not_found("b_condpag_mserv")
                self.click_relative(71, 359)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                if not self.find( "b_cfop_meserv", matching=0.97, waiting_time=10000):
                    self.not_found("b_cfop_meserv")
                self.click_relative(74, 403)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                if not self.find( "b_item_meserv", matching=0.97, waiting_time=10000):
                    self.not_found("b_item_meserv")
                self.click_relative(72, 444)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                if not self.find( "b_class_meserv", matching=0.97, waiting_time=10000):
                    self.not_found("b_class_meserv")
                self.click_relative(473, 322)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                if not self.find( "b_transportador_meserv", matching=0.97, waiting_time=10000):
                    self.not_found("b_transportador_meserv")
                self.click_relative(471, 362)
                self.type_keys_with_interval(1,'0081260')
                self.enter()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                if not self.find( "b_centrocustoserv_meserv", matching=0.97, waiting_time=10000):
                    self.not_found("b_centrocustoserv_meserv")
                self.click_relative(493, 402)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                if not self.find( "b_servico_meserv", matching=0.97, waiting_time=10000):
                    self.not_found("b_servico_meserv")
                self.click_relative(473, 445)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                self.enter()
                if not self.find( "b_vendedor_meserv", matching=0.97, waiting_time=10000):
                    self.not_found("b_vendedor_meserv")
                self.click_relative(873, 319)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                self.tab()
                self.tab()
                self.backspace()
                self.tab()

                if not self.find( "b_rota_meserv", matching=0.97, waiting_time=10000):
                    self.not_found("b_rota_meserv")
                self.click_relative(873, 363)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                if not self.find( "b_centrocustoitem_meserv", matching=0.97, waiting_time=10000):
                    self.not_found("b_centrocustoitem_meserv")
                self.click_relative(893, 403)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                self.wait(2000)
                self.type_keys_with_interval(1,'8748')
                self.tab()
                self.type_keys_with_interval(1,'99')
                self.tab()
                self.type_keys_with_interval(1,'99')
                self.tab()
                x=0
                while x<40:
                    self.type_down()
                    x=x+1
                x=0
                while x<39:
                    self.type_up()
                    x=x+1
                self.tab()
                x=0
                while x<12:
                    self.type_down()
                    x=x+1
                x=0
                while x<12:
                    self.type_up()
                    x=x+1
                self.tab()
                if not self.find( "b_codoperacao_MI_estoque", matching=0.97, waiting_time=10000):
                    self.not_found("b_codoperacao_MI_estoque")
                self.click_relative(68, 158)
                self.enter()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "b_cfop_MI_estoque", matching=0.97, waiting_time=10000):
                    self.not_found("b_cfop_MI_estoque")
                self.click_relative(68, 199)
                self.backspace()
                self.enter()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "b_condpag_MI_estoque", matching=0.97, waiting_time=10000):
                    self.not_found("b_condpag_MI_estoque")
                self.click_relative(433, 197)
                self.enter()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "b_fornecedor_MI_estoque", matching=0.97, waiting_time=10000):
                    self.not_found("b_fornecedor_MI_estoque")
                self.click_relative(210, 298)
                self.wait(2000)
                self.enter()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "b_comprador_MI_estoque", matching=0.97, waiting_time=10000):
                    self.not_found("b_comprador_MI_estoque")
                self.click_relative(439, 439)
                self.wait(2000)
                self.enter()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "b_rota_MI_estoque", matching=0.97, waiting_time=10000):
                    self.not_found("b_rota_MI_estoque")
                self.click_relative(68, 479)
                self.enter()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.tab()
                self.tab()
                self.tab()
                x=0
                while x<8:
                    self.type_down()
                    x=x+1
                x=0
                while x<8:
                    self.type_up()
                    x=x+1
                self.tab()
                x=0
                while x<5:
                    self.type_down()
                    x=x+1
                x=0
                while x<5:
                    self.type_up()
                    x=x+1
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                if not self.find( "b_centrocusto_MI_estoque", matching=0.97, waiting_time=10000):
                    self.not_found("b_centrocusto_MI_estoque")
                self.click_relative(82, 26)
                self.backspace()
                self.enter()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.tab()
                self.backspace()
                self.tab()
                if not self.find( "b_transportador_MI_estoque", matching=0.97, waiting_time=10000):
                    self.not_found("b_transportador_MI_estoque")
                self.click_relative(66, 25)
                self.enter()
                self.wait(1000)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.tab()
                self.tab()
                self.type_up()
                x=0
                while x<5:
                    self.type_down()
                    x=x+1
                x=0
                while x<4:
                    self.type_up()
                    x=x+1
                self.tab()
                if not self.find( "b_municipiocoleta_MI_estoque", matching=0.97, waiting_time=10000):
                    self.not_found("b_municipiocoleta_MI_estoque")
                self.click_relative(56, 25)
                self.tab()
                self.tab()
                self.tab()
                self.type_down()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "b_municipioentrega_MI_estoque", matching=0.97, waiting_time=10000):
                    self.not_found("b_municipioentrega_MI_estoque")
                self.click_relative(59, 24)
                self.tab()
                self.tab()
                self.tab()
                self.type_down()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.tab()
                self.tab()
                if not self.find( "b_classificacao_MI_estoque", matching=0.97, waiting_time=10000):
                    self.not_found("b_classificacao_MI_estoque")
                self.click_relative(57, 25)
                self.backspace()
                self.enter()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.tab()
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "aba2_MI_estoque", matching=0.97, waiting_time=10000):
                    self.not_found("aba2_MI_estoque")
                self.click()
                if not self.find( "incluir_movimentoitens_MI_estoque", matching=0.97, waiting_time=10000):
                    self.not_found("incluir_movimentoitens_MI_estoque")
                self.click_relative(14, 141)
                self.enter()
                if not self.find( "buscaritensreqcompras", matching=0.97, waiting_time=10000):
                    self.not_found("buscaritensreqcompras")
                self.click_relative(10, 31)
                self.type_keys_with_interval(1,'agulha gengival')
                self.enter()
                self.type_down()
                self.type_down()
                self.type_down()
                self.type_down()
                self.wait(500)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.type_keys_with_interval(1,'1')
                if not self.find( "botaoconfirmaritensreqcompras", matching=0.97, waiting_time=10000):
                    self.not_found("botaoconfirmaritensreqcompras")
                self.click()
                self.wait(3000)
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.tab()
                self.tab()
                self.type_keys_with_interval(1,'123')
                self.tab()
                self.type_keys_with_interval(1,'1')
                self.tab()
                self.type_keys_with_interval(1,'123')
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "b_lotenumero_MI_estoque", matching=0.97, waiting_time=10000):
                    self.not_found("b_lotenumero_MI_estoque")
                self.click_relative(207, 194)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                    self.not_found("salvarrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                self.wait(1500)
                self.enter()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                self.wait(2000)
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                                ####---ABA3 MI_ESTOQUE---####
                
                if not self.find( "aba3_MI_estoque", matching=0.97, waiting_time=10000):
                    self.not_found("aba3_MI_estoque")
                self.click()
                if not self.find( "b_servico_MI_estoque_a3", matching=0.97, waiting_time=10000):
                    self.not_found("b_servico_MI_estoque_a3")
                self.click_relative(70, 152)
                self.type_down()
                self.enter()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.enter()
                self.tab()
                self.tab()
                self.tab()
                self.type_keys_with_interval(1,'1')
                if not self.find( "b_classificacao_MI_estoque_a3", matching=0.97, waiting_time=10000):
                    self.not_found("b_classificacao_MI_estoque_a3")
                self.click_relative(72, 241)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                #if not self.find( "b_centrocusto_MI_estoque_a3", matching=0.97, waiting_time=10000):
                #    self.not_found("b_centrocusto_MI_estoque_a3")
                #self.click_relative(512, 200)
                #if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                #    self.not_found("retornarpe")
                #self.click()
                if not self.find( "gravar_a3_MI_estoque", matching=0.97, waiting_time=10000):
                    self.not_found("gravar_a3_MI_estoque")
                self.click()
                self.enter()
                #if not self.find( "b_cfop_MI_estoque_a3", matching=0.97, waiting_time=10000):
                #    self.not_found("b_cfop_MI_estoque_a3")
                #self.click_relative(75, 203)
                #if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #    self.not_found("selecionarmunicipiovcr")
                #self.click()
                self.wait(500)
                self.tab()
                self.tab()
                self.type_keys_with_interval(1,'123')
                #x=0
                #while x<6:
                #    if not self.find( "loop_tipotributacao_MI_estoque_a3", matching=0.97, waiting_time=10000):
                #        self.not_found("loop_tipotributacao_MI_estoque_a3")
                #    self.click_relative(396, 260)
                #    self.type_down()
                #    self.enter()
                #    x=x+1
                # 
                # x=0
                # while x<21:
                #     self.type_down()
                #     x=x+1
                # x=0
                # while x<6:
                #     if not self.find( "loop_tipotributacao2_MI_estoque_a3", matching=0.97, waiting_time=10000):
                #         self.not_found("loop_tipotributacao2_MI_estoque_a3")
                #     self.click_relative(397, 311)
                #     self.type_down()
                #     self.enter()
                #     x=x+1
                # x=0
                # while x<33:
                #     self.type_down()
                #     x=x+1
                # self.tab()
                # x=0
                # while x<4:
                #     self.type_down()
                #     x=x+1
                # x=0
                # while x<6:
                #     if not self.find( "loop_tipotributacao3_MI_estoque_a3", matching=0.97, waiting_time=10000):
                #         self.not_found("loop_tipotributacao3_MI_estoque_a3")
                #     self.click_relative(397, 348)
                #     self.type_down()
                #     self.enter()
                #     x=x+1
                # x=0
                # while x<33:
                #     self.type_down()
                #     x=x+1
                # self.tab()
                # x=0
                # while x<19:
                #     self.type_down()
                #     x=x+1
                # if not self.find( "b_centrocusto_MI_estoque_a3", matching=0.97, waiting_time=10000):
                #     self.not_found("b_centrocusto_MI_estoque_a3")
                # self.click_relative(96, 453)
                # if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                #     self.not_found("retornarfim")
                # self.click()
                # 
                self.enter()
                #if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                #    self.not_found("retornarpe")
                #self.click()
                #if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                #    self.not_found("salvarrs")
                #self.click()
                self.wait(1000)
                self.key_esc()
                #self.enter()
                self.wait(1000)
                if not self.find( "aba4_MI_estoque", matching=0.97, waiting_time=10000):
                    self.not_found("aba4_MI_estoque")
                self.click()
                if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                    self.not_found("salvarrs")
                self.click()
                self.enter()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "aba3_todos_estoque", matching=0.97, waiting_time=10000):
                    self.not_found("aba3_todos_estoque")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                    self.not_found("editarfim")
                self.click()
                #if not self.find( "desliberar_movItens_testesubs", matching=0.97, waiting_time=10000):
                #    self.not_found("desliberar_movItens_testesubs")
                #self.click()
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                                ####---ENTRADA E SAIDA RAPIDA---####
                
                if not self.find( "estoque4.1", matching=0.97, waiting_time=10000):
                    self.not_found("estoque4.1")
                self.click()
                if not self.find( "entradasaidarapida_estoque", matching=0.97, waiting_time=10000):
                    self.not_found("entradasaidarapida_estoque")
                self.click()
                self.wait(2000)
                self.enter()
                if not self.find( "aba2_estoque_entradasaidaserv", matching=0.97, waiting_time=10000):
                    self.not_found("aba2_estoque_entradasaidaserv")
                self.click()
                if not self.find( "a_cliente_MESIS_estoque", matching=0.97, waiting_time=10000):
                    self.not_found("a_cliente_MESIS_estoque")
                self.click_relative(521, 88)
                if not self.find( "b_cliente_MESIS_estoque", matching=0.97, waiting_time=10000):
                    self.not_found("b_cliente_MESIS_estoque")
                self.click_relative(512, 116)
                self.enter()
                x=0
                while x<18:
                    self.type_down()
                    x=x+1
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                self.tab()
                
                # if not self.find( "b_codop_MESIS_estoque", matching=0.97, waiting_time=10000):
                #     self.not_found("b_codop_MESIS_estoque")
                # self.click_relative(63, 41)
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # self.wait(500)
                # self.backspace()
                # if not self.find( "b_condpag_MESIS_estoque", matching=0.97, waiting_time=10000):
                #     self.not_found("b_condpag_MESIS_estoque")
                # self.click_relative(64, 81)
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # self.wait(500)
                # self.backspace()
                # if not self.find( "b_cfop_MESIS_estoque", matching=0.97, waiting_time=10000):
                #     self.not_found("b_cfop_MESIS_estoque")
                # self.click_relative(64, 126)
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # self.wait(500)
                # self.backspace()
                # if not self.find( "b_item_MESIS_estoque", matching=0.97, waiting_time=10000):
                #     self.not_found("b_item_MESIS_estoque")
                # self.click_relative(65, 167)
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # self.wait(500)
                # self.backspace()
                
                if not self.find( "b_codop_meserv", matching=0.97, waiting_time=10000):
                    self.not_found("b_codop_meserv")
                self.click_relative(74, 321)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                if not self.find( "b_condpag_mserv", matching=0.97, waiting_time=10000):
                    self.not_found("b_condpag_mserv")
                self.click_relative(71, 359)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                if not self.find( "b_cfop_meserv", matching=0.97, waiting_time=10000):
                    self.not_found("b_cfop_meserv")
                self.click_relative(74, 403)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                if not self.find( "b_item_meserv", matching=0.97, waiting_time=10000):
                    self.not_found("b_item_meserv")
                self.click_relative(72, 444)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                if not self.find( "b_class_meserv", matching=0.97, waiting_time=10000):
                    self.not_found("b_class_meserv")
                self.click_relative(473, 322)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                if not self.find( "b_transportador_meserv", matching=0.97, waiting_time=10000):
                    self.not_found("b_transportador_meserv")
                self.click_relative(471, 362)
                self.type_keys_with_interval(1,'0081260')
                self.enter()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                if not self.find( "b_centrocustoserv_meserv", matching=0.97, waiting_time=10000):
                    self.not_found("b_centrocustoserv_meserv")
                self.click_relative(493, 402)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                if not self.find( "b_servico_meserv", matching=0.97, waiting_time=10000):
                    self.not_found("b_servico_meserv")
                self.click_relative(473, 445)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                if not self.find( "b_vendedor_meserv", matching=0.97, waiting_time=10000):
                    self.not_found("b_vendedor_meserv")
                self.click_relative(873, 319)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.enter()
                self.wait(500)
                self.backspace()
                self.backspace()
                self.tab()
                self.tab()
                if not self.find( "b_rota_meserv", matching=0.97, waiting_time=10000):
                    self.not_found("b_rota_meserv")
                self.click_relative(873, 363)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                if not self.find( "b_centrocustoitem_meserv", matching=0.97, waiting_time=10000):
                    self.not_found("b_centrocustoitem_meserv")
                self.click_relative(893, 403)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                self.wait(2000)
                if not self.find( "b_codigoOperacao_MRI", matching=0.97, waiting_time=10000):
                    self.not_found("b_codigoOperacao_MRI")
                self.click_relative(66, 160)
                self.enter()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "b_cliente_MRI", matching=0.97, waiting_time=10000):
                    self.not_found("b_cliente_MRI")
                self.click_relative(68, 198)
                self.enter()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.tab()
                self.wait(500)
                
                # if not self.find( "b_centroCusto_MRI", matching=0.97, waiting_time=10000):
                #     self.not_found("b_centroCusto_MRI")
                # self.click_relative(90, 242)
                # self.backspace()
                # self.enter()
                # if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #     self.not_found("selecionarmunicipiovcr")
                # self.click()
                # self.wait(500)
                # self.tab()
                # self.backspace()            
                #if not self.find( "b_operacao_MRI_estoque", matching=0.97, waiting_time=10000):
                #    self.not_found("b_operacao_MRI_estoque")
                #self.click_relative(483, 107)
                #self.enter()
                #if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #    self.not_found("selecionarmunicipiovcr")
                #self.click()
                #self.wait(500)
                #x=0
                #while x<6:
                #    self.tab()
                #    x=x+1
                #self.type_keys_with_interval(1,'te12!@')
                if not self.find( "ir_MRI_estoquerapido", matching=0.97, waiting_time=10000):
                    self.not_found("ir_MRI_estoquerapido")
                self.click_relative(11, 325)
                if not self.find( "buscaritensreqcompras", matching=0.97, waiting_time=10000):
                    self.not_found("buscaritensreqcompras")
                self.click_relative(10, 31)
                self.type_keys_with_interval(1,'agulha gengival')
                self.enter()
                self.type_down()
                self.type_down()
                self.type_down()
                self.type_down()
                self.wait(500)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.type_keys_with_interval(1,'1')
                if not self.find( "botaoconfirmaritensreqcompras", matching=0.97, waiting_time=10000):
                    self.not_found("botaoconfirmaritensreqcompras")
                self.click()
                self.wait(3000)
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.tab()
                self.tab()
                self.type_keys_with_interval(1,'123')
                self.tab()
                self.type_keys_with_interval(1,'1')
                self.tab()
                self.type_keys_with_interval(1,'123')
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "b_lotenumero_MI_estoque", matching=0.97, waiting_time=10000):
                    self.not_found("b_lotenumero_MI_estoque")
                self.click_relative(207, 194)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                    self.not_found("salvarrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                self.wait(2000)
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                    self.not_found("salvarrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "a2_selecao_testeG", matching=0.97, waiting_time=10000):
                    self.not_found("a2_selecao_testeG")
                self.click_relative(57, 147)
                if not self.find( "apagar_vendedor_testeG", matching=0.97, waiting_time=10000):
                    self.not_found("apagar_vendedor_testeG")
                self.double_click_relative(835, 41)
                self.backspace()
                if not self.find( "aba3_todos_estoque", matching=0.97, waiting_time=10000):
                    self.not_found("aba3_todos_estoque")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                    self.not_found("editarfim")
                self.click()
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                                ####---ALMOXARIFADO---####
                                
                if not self.find( "estoque4.1", matching=0.97, waiting_time=10000):
                    self.not_found("estoque4.1")
                self.click()
                if not self.find( "almoxarifado", matching=0.97, waiting_time=10000):
                    self.not_found("almoxarifado")
                self.click()
                if not self.find( "almoxarifado", matching=0.97, waiting_time=10000):
                    self.not_found("almoxarifado")
                self.click()
                self.wait(3000)
                self.enter()
                if not self.find( "aba2_estoque_entradasaidaserv", matching=0.97, waiting_time=10000):
                    self.not_found("aba2_estoque_entradasaidaserv")
                self.click()
                if not self.find( "b_codop_MESIS_estoque", matching=0.97, waiting_time=10000):
                    self.not_found("b_codop_MESIS_estoque")
                self.click_relative(63, 41)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                if not self.find( "b_condpag_MESIS_estoque", matching=0.97, waiting_time=10000):
                    self.not_found("b_condpag_MESIS_estoque")
                self.click_relative(64, 81)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                if not self.find( "b_cfop_MESIS_estoque", matching=0.97, waiting_time=10000):
                    self.not_found("b_cfop_MESIS_estoque")
                self.click_relative(64, 126)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                if not self.find( "b_item_MESIS_estoque", matching=0.97, waiting_time=10000):
                    self.not_found("b_item_MESIS_estoque")
                self.click_relative(65, 167)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                if not self.find( "b_classificacao_CMIA_almoxarifado", matching=0.97, waiting_time=10000):
                    self.not_found("b_classificacao_CMIA_almoxarifado")
                self.click_relative(464, 44)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                if not self.find( "b_transportador_CMIA_almoxarifado", matching=0.97, waiting_time=10000):
                    self.not_found("b_transportador_CMIA_almoxarifado")
                self.click_relative(465, 82)
                self.enter()
                self.type_down()
                self.type_down()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                if not self.find( "b_centrocusto_servico_CMIA_almoxarifado", matching=0.97, waiting_time=10000):
                    self.not_found("b_centrocusto_servico_CMIA_almoxarifado")
                self.click_relative(485, 126)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                if not self.find( "b_servico_CMIA_almoxarifado", matching=0.97, waiting_time=10000):
                    self.not_found("b_servico_CMIA_almoxarifado")
                self.click_relative(467, 167)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                self.enter()
                if not self.find( "b_vendedor_CMIA_almoxarifado", matching=0.97, waiting_time=10000):
                    self.not_found("b_vendedor_CMIA_almoxarifado")
                self.click_relative(865, 41)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                if not self.find( "b_rota_CMIA_almoxarifado", matching=0.97, waiting_time=10000):
                    self.not_found("b_rota_CMIA_almoxarifado")
                self.click_relative(861, 85)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                if not self.find( "b_centrocusto_itens_CMIA_almoxarifado", matching=0.97, waiting_time=10000):
                    self.not_found("b_centrocusto_itens_CMIA_almoxarifado")
                self.click_relative(886, 123)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                self.wait(2000)
                self.tab()
                self.type_keys_with_interval(1,'123')            
                if not self.find( "b_operacao_MA_almoxarifado", matching=0.97, waiting_time=10000):
                    self.not_found("b_operacao_MA_almoxarifado")
                self.click_relative(63, 160)
                if not self.find( "aba2_selecao_teste1", matching=0.97, waiting_time=10000):
                    self.not_found("aba2_selecao_teste1")
                self.click()
                if not self.find( "todos_selecao_teste1", matching=0.97, waiting_time=10000):
                    self.not_found("todos_selecao_teste1")
                self.click_relative(-4, 248)
                self.tab()
                self.tab()
                self.type_keys_with_interval(1,'22')
                self.enter()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "b_centrodecusto_MA_almoxarifado", matching=0.97, waiting_time=10000):
                    self.not_found("b_centrodecusto_MA_almoxarifado")
                self.click_relative(96, 204)
                self.backspace()
                self.enter()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.tab()
                self.backspace()
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "ir_MA_almoxarifado", matching=0.97, waiting_time=10000):
                    self.not_found("ir_MA_almoxarifado")
                self.click_relative(14, 334)
                if not self.find( "buscaritensreqcompras", matching=0.97, waiting_time=10000):
                    self.not_found("buscaritensreqcompras")
                self.click_relative(10, 31)
                self.type_keys_with_interval(1,'agulha gengival')
                self.enter()
                self.type_down()
                self.type_down()
                self.type_down()
                self.type_down()
                self.wait(500)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.type_keys_with_interval(1,'1')
                if not self.find( "botaoconfirmaritensreqcompras", matching=0.97, waiting_time=10000):
                    self.not_found("botaoconfirmaritensreqcompras")
                self.click()
                self.wait(3000)
                #if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                #    self.not_found("incluirpe")
                #self.click()
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.tab()
                self.tab()
                self.type_keys_with_interval(1,'123')
                self.tab()
                self.type_keys_with_interval(1,'1')
                self.tab()
                self.type_keys_with_interval(1,'123')
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "b_lotenumero_MI_almoxarifado_2.0", matching=0.97, waiting_time=10000):
                    self.not_found("b_lotenumero_MI_almoxarifado_2.0")
                self.click_relative(207, 192)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                    self.not_found("salvarrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                self.wait(2000)
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                    self.not_found("salvarrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "aba3_todos_estoque", matching=0.97, waiting_time=10000):
                    self.not_found("aba3_todos_estoque")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                    self.not_found("editarfim")
                self.click()
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                                ####---ALMOXARIFADO OSM SAIDA---####
                                
                if not self.find( "estoque4.1", matching=0.97, waiting_time=10000):
                    self.not_found("estoque4.1")
                self.click()
                if not self.find( "almoxarifado", matching=0.97, waiting_time=10000):
                    self.not_found("almoxarifado")
                self.click()
                if not self.find( "almoxarifadoOSMsaida", matching=0.97, waiting_time=10000):
                    self.not_found("almoxarifadoOSMsaida")
                self.click()
                if not self.find( "b_classificacao_saida_almoxarifado", matching=0.97, waiting_time=10000):
                    self.not_found("b_classificacao_saida_almoxarifado")
                self.click_relative(91, 313)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "aba2_consulta_saida_almoxarifado", matching=0.97, waiting_time=10000):
                    self.not_found("aba2_consulta_saida_almoxarifado")
                self.click()
                if not self.find( "b_cliente_saida_almoxarifado", matching=0.97, waiting_time=10000):
                    self.not_found("b_cliente_saida_almoxarifado")
                self.click_relative(298, 141)
                self.enter()
                x=0
                while x<18:
                    self.type_down()
                    x=x+1
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "b_projeto_saida_almoxarifado", matching=0.97, waiting_time=10000):
                    self.not_found("b_projeto_saida_almoxarifado")
                self.click_relative(986, 140)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.enter()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                                ####---ALMOXARIFADO OSM DEVOLUCAO---####
                                
                if not self.find( "estoque4.1", matching=0.97, waiting_time=10000):
                    self.not_found("estoque4.1")
                self.click()
                if not self.find( "almoxarifado", matching=0.97, waiting_time=10000):
                    self.not_found("almoxarifado")
                self.click()
                if not self.find( "almoxarifadoOSMdevolucao", matching=0.97, waiting_time=10000):
                    self.not_found("almoxarifadoOSMdevolucao")
                self.click()
                if not self.find( "b_entrada_almoxarifado_padrao", matching=0.97, waiting_time=10000):
                    self.not_found("b_entrada_almoxarifado_padrao")            
                self.click_relative(91, 313)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "aba2_consulta_saida_almoxarifado", matching=0.97, waiting_time=10000):
                    self.not_found("aba2_consulta_saida_almoxarifado")
                self.click()
                if not self.find( "b_entrada_almoxarifado_padrao", matching=0.97, waiting_time=10000):
                    self.not_found("b_entrada_almoxarifado_padrao")
                self.click_relative(298, 141)
                self.enter()
                x=0
                while x<18:
                    self.type_down()
                    x=x+1
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "b_entrada_almoxarifado_padrao", matching=0.97, waiting_time=10000):
                    self.not_found("b_entrada_almoxarifado_padrao")
                self.click_relative(986, 140)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.enter()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                                ####---SOLICITAÇÃO---####
                                
                if not self.find( "estoque4.1", matching=0.97, waiting_time=10000):
                    self.not_found("estoque4.1")
                self.click()
                if not self.find( "almoxarifado", matching=0.97, waiting_time=10000):
                    self.not_found("almoxarifado")
                self.click()
                if not self.find( "solicitacao_almoxarifado", matching=0.97, waiting_time=10000):
                    self.not_found("solicitacao_almoxarifado")
                self.click()
                if not self.find( "selecao_solicitacao_almoxarifado", matching=0.97, waiting_time=10000):
                    self.not_found("selecao_solicitacao_almoxarifado")
                self.click()
                if not self.find( "b_item_solicitacao_almoxarifado", matching=0.97, waiting_time=10000):
                    self.not_found("b_item_solicitacao_almoxarifado")
                self.click_relative(73, 165)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                self.tab()
                if not self.find( "b_classificacao_solicitacao_almoxarifado", matching=0.97, waiting_time=10000):
                    self.not_found("b_classificacao_solicitacao_almoxarifado")
                self.click_relative(67, 212)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                self.tab()
                if not self.find( "b_centrocusto_solicitacao_almoxarifado", matching=0.97, waiting_time=10000):
                    self.not_found("b_centrocusto_solicitacao_almoxarifado")
                self.click_relative(474, 213)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                self.tab()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()  
                if not self.find( "b_solicitante_solicitacao_almoxarifado", matching=0.97, waiting_time=10000):
                    self.not_found("b_solicitante_solicitacao_almoxarifado")
                self.click_relative(62, 150)
                self.type_keys_with_interval(1,'cadastro')
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "b_cliente_solicitacao_almoxarifado", matching=0.97, waiting_time=10000):
                    self.not_found("b_cliente_solicitacao_almoxarifado")
                self.click_relative(510, 149)
                self.enter()
                x=0
                while x<18:
                    self.type_down()
                    x=x+1
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)     
                self.tab()
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "ir_solicitacao_almoxarifado", matching=0.97, waiting_time=10000):
                    self.not_found("ir_solicitacao_almoxarifado")
                self.click_relative(14, 264)
                if not self.find( "buscaritensreqcompras", matching=0.97, waiting_time=10000):
                    self.not_found("buscaritensreqcompras")
                self.click_relative(10, 31)
                self.type_keys_with_interval(1,'agulha gengival')
                self.enter()
                self.type_down()
                self.type_down()
                self.type_down()
                self.type_down()
                self.wait(500)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.type_keys_with_interval(1,'1')
                if not self.find( "botaoconfirmaritensreqcompras", matching=0.97, waiting_time=10000):
                    self.not_found("botaoconfirmaritensreqcompras")
                self.click()
                self.wait(3000)
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                    self.not_found("salvarrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                self.wait(2000)
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                    self.not_found("editarfim")
                self.click()
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()

                                ####---INVENTÁRIO---####

                if not self.find( "estoque4.1", matching=0.97, waiting_time=10000):
                    self.not_found("estoque4.1")
                self.click()
                if not self.find( "inventario_estoque", matching=0.97, waiting_time=10000):
                    self.not_found("inventario_estoque")
                self.click()
                if not self.find( "selecao_solicitacao_almoxarifado", matching=0.97, waiting_time=10000):
                    self.not_found("selecao_solicitacao_almoxarifado")
                self.click()
                if not self.find( "b_item_inventario_estoque", matching=0.97, waiting_time=10000):
                    self.not_found("b_item_inventario_estoque")
                self.click_relative(73, 168)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                self.wait(500)
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.tab()
                self.tab()
                self.tab()
                self.type_down()
                self.type_up()
                self.type_up()
                self.type_down()
                self.tab()
                x=0
                while x<4:
                    self.type_down()
                    x=x+1
                x=0
                while x<4:
                    self.type_up()
                    x=x+1
                self.tab()
                self.type_down()
                self.type_up()
                self.tab()
                x=0
                while x<5:
                    self.type_down()
                    x=x+1
                x=0
                while x<5:
                    self.type_up()
                    x=x+1
                self.tab()
                if not self.find( "b_codigoclientefornecedor_inventario_estoque", matching=0.97, waiting_time=10000):
                    self.not_found("b_codigoclientefornecedor_inventario_estoque")
                self.click_relative(80, 238)
                self.enter()
                x=0
                while x<18:
                    self.type_down()
                    x=x+1
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "b_operacaoentrada_inventario_estoque", matching=0.97, waiting_time=10000):
                    self.not_found("b_operacaoentrada_inventario_estoque")
                self.click_relative(82, 279)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "b_operacaosaida_inventario_estoque", matching=0.97, waiting_time=10000):
                    self.not_found("b_operacaosaida_inventario_estoque")
                self.click_relative(82, 320)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "b_localestoque_inventario_estoque", matching=0.97, waiting_time=10000):
                    self.not_found("b_localestoque_inventario_estoque")
                self.click_relative(541, 280)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.enter()
                self.tab()
                self.tab()
                self.tab()
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "a2_inventario_estoque", matching=0.97, waiting_time=10000):
                    self.not_found("a2_inventario_estoque")
                self.click()
                if not self.find( "ir_a2p1_inventario_estoque", matching=0.97, waiting_time=10000):
                    self.not_found("ir_a2p1_inventario_estoque")
                self.click_relative(18, 164)
                if not self.find( "buscaritensreqcompras", matching=0.97, waiting_time=10000):
                    self.not_found("buscaritensreqcompras")
                self.click_relative(10, 31)
                self.type_keys_with_interval(1,'agulha gengival')
                self.enter()
                self.type_down()
                self.type_down()
                self.type_down()
                self.type_down()
                self.wait(500)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "botaoconfirmaritensreqcompras", matching=0.97, waiting_time=10000):
                    self.not_found("botaoconfirmaritensreqcompras")
                self.click()
                self.wait(3000)
                self.enter()
                self.space()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.enter()
                if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                    self.not_found("salvarrs")
                self.click()
                if not self.find( "a2p2_inventario_estoque", matching=0.97, waiting_time=10000):
                    self.not_found("a2p2_inventario_estoque")
                self.click()
                if not self.find( "ir_a2p2_inventario_estoque", matching=0.97, waiting_time=10000):
                    self.not_found("ir_a2p2_inventario_estoque")
                self.click_relative(19, 165)
                if not self.find( "buscaritensreqcompras", matching=0.97, waiting_time=10000):
                    self.not_found("buscaritensreqcompras")
                self.click_relative(10, 31)
                self.type_keys_with_interval(1,'agulha gengival')
                self.enter()
                self.type_down()
                self.type_down()
                self.type_down()
                self.type_down()
                self.wait(500)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "b_clientefornecedor_a2p2_inventario_estoque", matching=0.97, waiting_time=10000):
                    self.not_found("b_clientefornecedor_a2p2_inventario_estoque")
                self.click_relative(565, 277)
                self.wait(1000)
                self.enter()
                self.wait(1000)
                x=0
                while x<18:
                    self.type_down()
                    x=x+1
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "botaoconfirmaritensreqcompras", matching=0.97, waiting_time=10000):
                    self.not_found("botaoconfirmaritensreqcompras")
                self.click()
                self.wait(3000)
                self.enter()
                self.space()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.enter()
                if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                    self.not_found("salvarrs")
                self.click()
                if not self.find( "a2p3_inventario_estoque", matching=0.97, waiting_time=10000):
                    self.not_found("a2p3_inventario_estoque")
                self.click()
                if not self.find( "b_lancamentoporitem_inventario_estoque", matching=0.97, waiting_time=10000):
                    self.not_found("b_lancamentoporitem_inventario_estoque")
                self.click_relative(240, 207)
                self.type_keys_with_interval(1,'104455')
                self.enter()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "a2p4_inventario_estoque", matching=0.97, waiting_time=10000):
                    self.not_found("a2p4_inventario_estoque")
                self.click()
                if not self.find( "b_data_a2p4_inventario_estoque", matching=0.97, waiting_time=10000):
                    self.not_found("b_data_a2p4_inventario_estoque")
                self.click_relative(352, 201)
                if not self.find( "carregar_dia_a2p4", matching=0.97, waiting_time=10000):
                    self.not_found("carregar_dia_a2p4")
                self.click()
                if not self.find( "carregar_dia_atual_a2p4", matching=0.97, waiting_time=10000):
                    self.not_found("carregar_dia_atual_a2p4")
                self.click()
                self.tab()
                self.tab()
                self.space()
                self.space()
                self.tab()
                self.space()
                self.space()
                self.tab()
                self.type_keys_with_interval(1,'123')
                self.tab()
                self.space()
                self.space()
                self.tab()
                self.space()
                self.space()
                self.tab()
                self.space()
                self.space()
                self.tab()
                self.tab()
                self.tab()
                self.tab()
                self.space()
                self.space()
                if not self.find( "filtro_a2p4_inventario_estoque", matching=0.97, waiting_time=10000):
                    self.not_found("filtro_a2p4_inventario_estoque")
                self.click()
                if not self.find( "retornar_filtro_a2p4", matching=0.97, waiting_time=10000):
                    self.not_found("retornar_filtro_a2p4")
                self.click_relative(39, 40)
                if not self.find( "a3_inventario_estoque", matching=0.97, waiting_time=10000):
                    self.not_found("a3_inventario_estoque")
                self.click()
                self.tab()
                if not self.find( "a3_filtro_inventario_estoque", matching=0.97, waiting_time=10000):
                    self.not_found("a3_filtro_inventario_estoque")
                self.click_relative(52, 15)            
                if not self.find( "retornar_filtro_a2p4", matching=0.97, waiting_time=10000):
                    self.not_found("retornar_filtro_a2p4")
                self.click_relative(39, 40)
                self.tab()
                self.tab()
                self.type_down()
                self.type_up()
                self.tab()
                x=0
                while x<6:
                    self.type_down()
                    x=x+1
                x=0
                while x<6:
                    self.type_up()
                    x=x+1
                self.tab()
                self.space()
                self.space()
                if not self.find( "a4_inventario_estoque", matching=0.97, waiting_time=10000):
                    self.not_found("a4_inventario_estoque")
                self.click()
                self.tab()
                self.tab()
                x=0
                while x<4:
                    self.type_keys_with_interval(1,'123')
                    self.tab()
                    x=x+1
                if not self.find( "apagardescricao_inventario_estoque", matching=0.97, waiting_time=10000):
                    self.not_found("apagardescricao_inventario_estoque")
                self.click_relative(145, 88)
                x=0
                while x<6:
                    self.backspace()
                    x=x+1
                if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                    self.not_found("salvarrs")
                self.click()    
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                    self.not_found("editarfim")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                                ####---MANIFESTACAO DO DESTINATARIO---####

                if not self.find( "estoque4.1", matching=0.97, waiting_time=10000):
                    self.not_found("estoque4.1")
                self.click()
                if not self.find( "manifestacaododestinatario", matching=0.97, waiting_time=10000):
                    self.not_found("manifestacaododestinatario")
                self.click()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                x=0
                while x<3:
                    self.type_down()
                    x=x+1
                x=0
                while x<3:
                    self.type_up()
                    x=x+1
                self.tab()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                                ####---TRANSFORMACAO ITENS---#### 
                                        
                if not self.find( "estoque4.1", matching=0.97, waiting_time=10000):
                    self.not_found("estoque4.1")
                self.click()
                if not self.find( "transformacaodeitens", matching=0.97, waiting_time=10000):
                    self.not_found("transformacaodeitens")
                self.click()
                self.wait(1000)
                self.enter()
                if not self.find( "selecao_trans_itens", matching=0.97, waiting_time=10000):
                    self.not_found("selecao_trans_itens")
                self.click()
                if not self.find( "b_item_trans_itens", matching=0.97, waiting_time=10000):
                    self.not_found("b_item_trans_itens")
                self.click_relative(229, 154)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                self.tab()
                if not self.find( "b_clientepedido_trans_itens", matching=0.97, waiting_time=10000):
                    self.not_found("b_clientepedido_trans_itens")
                self.click_relative(69, 204)
                self.enter()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                self.tab()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                x=0
                while x<7:
                    self.tab()
                    x=x+1
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "ir_itens_trans_itens", matching=0.97, waiting_time=10000):
                    self.not_found("ir_itens_trans_itens")
                self.click_relative(17, 271)
                if not self.find( "buscaritensreqcompras", matching=0.97, waiting_time=10000):
                    self.not_found("buscaritensreqcompras")
                self.click_relative(10, 31)
                self.type_keys_with_interval(1,'agulha gengival')
                self.enter()
                self.type_down()
                self.type_down()
                self.type_down()
                self.type_down()
                self.wait(500)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.type_keys_with_interval(1,'1')
                if not self.find( "botaoconfirmaritensreqcompras", matching=0.97, waiting_time=10000):
                    self.not_found("botaoconfirmaritensreqcompras")
                self.click()
                self.wait(3000) 
                self.type_keys_with_interval(1,'123')
                self.tab()
                self.tab()
                self.type_keys_with_interval(1,'123')
                self.tab()
                self.tab()
                self.tab()
                self.type_keys_with_interval(1,'1')
                self.tab()
                self.type_keys_with_interval(1,'123')
                #if not self.find( "b_lotenumero_MI_estoque", matching=0.97, waiting_time=10000):
                #    self.not_found("b_lotenumero_MI_estoque")
                #self.click_relative(207, 194)
                #if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                #    self.not_found("selecionarmunicipiovcr")
                #self.click()
                self.wait(500)
                if not self.find( "b_lotenumero_inf_entradalote_2", matching=0.97, waiting_time=10000):
                    self.not_found("b_lotenumero_inf_entradalote_2")
                self.click_relative(206, 148)
                self.backspace()
                self.type_keys_with_interval(1,'123')
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                    self.not_found("salvarrs")
                self.click()
                self.wait(4000)
                #if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                #    self.not_found("retornarpe")
                #self.click()
                self.key_esc()
                self.wait(4000)
                self.enter()
                self.wait(4000)
                self.enter()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                self.wait(2000)
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                self.wait(2000)
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                    self.not_found("editarfim")
                self.click()
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                                ####---CADASTROS MODO DE TRANSFERENCIAS---####
                                
                if not self.find( "estoque4.1", matching=0.97, waiting_time=10000):
                    self.not_found("estoque4.1")
                self.click()
                if not self.find( "transferencias_estoque", matching=0.97, waiting_time=10000):
                    self.not_found("transferencias_estoque")
                self.click()
                if not self.find( "cadastros_modotransferencia_estoque", matching=0.97, waiting_time=10000):
                    self.not_found("cadastros_modotransferencia_estoque")
                self.click()
                self.backspace()
                self.enter()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "b_origem_empresa_modotrans", matching=0.97, waiting_time=10000):
                    self.not_found("b_origem_empresa_modotrans")
                self.click_relative(153, 143)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "b_origem_empresa_modotrans", matching=0.97, waiting_time=10000):
                    self.not_found("b_origem_empresa_modotrans")
                self.click_relative(153, 173)
                self.enter()
                x=0
                while x<18:
                    self.type_down()
                    x=x+1
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "b_origem_empresa_modotrans", matching=0.97, waiting_time=10000):
                    self.not_found("b_origem_empresa_modotrans")
                self.click_relative(153, 203)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "b_origem_empresa_modotrans", matching=0.97, waiting_time=10000):
                    self.not_found("b_origem_empresa_modotrans")
                self.click_relative(153, 293)
                self.enter()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "b_origem_empresa_modotrans", matching=0.97, waiting_time=10000):
                    self.not_found("b_origem_empresa_modotrans")
                self.click_relative(153, 313)
                self.enter()
                x=0
                while x<18:
                    self.type_down()
                    x=x+1
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "b_origem_empresa_modotrans", matching=0.97, waiting_time=10000):
                    self.not_found("b_origem_empresa_modotrans")
                self.click_relative(153, 333)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)    
                if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                    self.not_found("salvarrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "codigo_teste_modotrans", matching=0.97, waiting_time=10000):
                    self.not_found("codigo_teste_modotrans")
                self.click()
                if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                    self.not_found("editarfim")
                self.click()
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                                ####---MOVIMENTO TRANSFERENCIA---####
                                
                if not self.find( "estoque4.1", matching=0.97, waiting_time=10000):
                    self.not_found("estoque4.1")
                self.click()
                if not self.find( "transferencias_estoque", matching=0.97, waiting_time=10000):
                    self.not_found("transferencias_estoque")
                self.click()
                if not self.find( "movimentodetransferencia_estq", matching=0.97, waiting_time=10000):
                    self.not_found("movimentodetransferencia_estq")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                if not self.find( "b_modotransferencia_estoque", matching=0.97, waiting_time=10000):
                    self.not_found("b_modotransferencia_estoque")
                self.click_relative(80, 156)
                self.enter()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500) 
                if not self.find( "b_vendedor_movtransitens", matching=0.97, waiting_time=10000):
                    self.not_found("b_vendedor_movtransitens")
                self.click_relative(82, 246)
                self.enter()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500) 
                if not self.find( "b_condpag_movtransitens", matching=0.97, waiting_time=10000):
                    self.not_found("b_condpag_movtransitens")
                self.click_relative(82, 290)
                self.enter()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500) 
                self.tab()
                self.tab()
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "ir_movtransitens", matching=0.97, waiting_time=10000):
                    self.not_found("ir_movtransitens")
                self.click_relative(17, 317)
                if not self.find( "buscaritensreqcompras", matching=0.97, waiting_time=10000):
                    self.not_found("buscaritensreqcompras")
                self.click_relative(10, 31)
                self.type_keys_with_interval(1,'agulha gengival')
                self.enter()
                self.type_down()
                self.type_down()
                self.type_down()
                self.type_down()
                self.wait(500)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.type_keys_with_interval(1,'1')
                self.tab()
                self.type_keys_with_interval(1,'7')
                self.tab()
                if not self.find( "botaoconfirmaritensreqcompras", matching=0.97, waiting_time=10000):
                    self.not_found("botaoconfirmaritensreqcompras")
                self.click()
                self.type_keys_with_interval(1,'123')
                self.tab()
                self.tab()
                self.type_keys_with_interval(1,'123')
                self.tab()
                self.tab()
                self.tab()
                self.type_keys_with_interval(1,'1')
                self.tab()
                self.type_keys_with_interval(1,'123')
                if not self.find( "b_numerolote_movtransitens", matching=0.97, waiting_time=10000):
                    self.not_found("b_numerolote_movtransitens")
                self.click_relative(204, 193)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                    self.not_found("salvarrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                self.wait(2000)
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                self.wait(2000)
                if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                    self.not_found("salvarrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                self.wait(2000)
                if not self.find( "op_todas_consultaTransItens", matching=0.97, waiting_time=10000):
                    self.not_found("op_todas_consultaTransItens")
                self.click()
                            
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                    self.not_found("editarfim")
                self.click()
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                                ####---DEVOLUCOES CLIENTES---####
                                
                if not self.find( "estoque4.1", matching=0.97, waiting_time=10000):
                    self.not_found("estoque4.1")
                self.click()
                if not self.find( "devolucoesclientes_estoque", matching=0.97, waiting_time=10000):
                    self.not_found("devolucoesclientes_estoque")
                self.click()
                if not self.find( "aba2_consultadevolucaoitens", matching=0.97, waiting_time=10000):
                    self.not_found("aba2_consultadevolucaoitens")
                self.click()
                if not self.find( "b_operacao_devitens", matching=0.97, waiting_time=10000):
                    self.not_found("b_operacao_devitens")
                self.click_relative(72, 151)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                self.tab()
                if not self.find( "b_condpagamento_devitens", matching=0.97, waiting_time=10000):
                    self.not_found("b_condpagamento_devitens")
                self.click_relative(71, 190)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                self.tab()
                if not self.find( "b_itens_devitens", matching=0.97, waiting_time=10000):
                    self.not_found("b_itens_devitens")
                self.click_relative(71, 226)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                self.tab()
                if not self.find( "b_vendedor_devitens", matching=0.97, waiting_time=10000):
                    self.not_found("b_vendedor_devitens")
                self.click_relative(460, 188)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.backspace()
                self.tab()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not bot.find( "fatu_btn_incluir_opc_1_2411", matching=0.97, waiting_time=10000):
                    not_found("fatu_btn_incluir_opc_1_2411")
                bot.click()
                if not self.find( "b_operacao_devitens_pdv", matching=0.97, waiting_time=10000):
                    self.not_found("b_operacao_devitens_pdv")
                self.click_relative(83, 149)
                self.backspace()
                self.type_keys_with_interval(1,'0014')
                self.enter()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "b_vendedor_devitens_pdv", matching=0.97, waiting_time=10000):
                    self.not_found("b_vendedor_devitens_pdv")
                self.click_relative(83, 193)
                self.enter()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "b_condpagamento_devitens_pdv", matching=0.97, waiting_time=10000):
                    self.not_found("b_condpagamento_devitens_pdv")
                self.click_relative(84, 237)
                self.enter()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.tab()
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "b_clientefornecedor_devitens_pdv", matching=0.97, waiting_time=10000):
                    self.not_found("b_clientefornecedor_devitens_pdv")
                self.click_relative(482, 149)
                self.enter()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "ir_devitens_pdv", matching=0.97, waiting_time=10000):
                    self.not_found("ir_devitens_pdv")
                self.click_relative(17, 311)
                if not self.find( "buscaritensreqcompras", matching=0.97, waiting_time=10000):
                    self.not_found("buscaritensreqcompras")
                self.click_relative(10, 31)
                self.type_keys_with_interval(1,'agulha gengival')
                self.enter()
                self.type_down()
                self.type_down()
                self.type_down()
                self.type_down()
                self.wait(500)
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                self.type_keys_with_interval(1,'1')
                self.tab()
                if not self.find( "botaoconfirmaritensreqcompras", matching=0.97, waiting_time=10000):
                    self.not_found("botaoconfirmaritensreqcompras")
                self.click()
                self.type_keys_with_interval(1,'123')
                self.tab()
                self.type_keys_with_interval(1,'123')
                self.tab()
                self.tab()
                self.tab()
                self.type_keys_with_interval(1,'1')
                self.tab()
                self.type_keys_with_interval(1,'123')
                if not self.find( "b_lotenumero_inf_entradalote", matching=0.97, waiting_time=10000):
                    self.not_found("b_lotenumero_inf_entradalote")
                self.double_click_relative(46, 150)
                self.backspace()
                self.type_keys_with_interval(1,'123')
                if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                    self.not_found("salvarrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                self.wait(2000)
                self.enter()
                self.wait(4000)
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                self.wait(2000)
                if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                    self.not_found("salvarrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                self.wait(2000)
                if not self.find( "op_todas_movtransitens", matching=0.97, waiting_time=10000):
                    self.not_found("op_todas_movtransitens")
                self.click()            
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                    self.not_found("editarfim")
                self.click()
                if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("excluirrs")
                self.click()
                if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                    self.not_found("simexcluirrs")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                    self.not_found("localizarfim")
                self.click()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                
                                ####---FICHA CONTEUDO IMPORTACAO---####
                                
                if not self.find( "estoque4.1", matching=0.97, waiting_time=10000):
                    self.not_found("estoque4.1")
                self.click()
                if not self.find( "FCI_estoque", matching=0.97, waiting_time=10000):
                    self.not_found("FCI_estoque")
                self.click()
                self.enter()
                if not self.find( "ir_movimentoFCI", matching=0.97, waiting_time=10000):
                    self.not_found("ir_movimentoFCI")
                self.click_relative(15, 334)
                x=0
                while x<12:
                    self.type_down()
                    x=x+1
                self.tab()
                x=0
                while x<4:
                    self.type_keys_with_interval(1,'123')
                    self.tab()
                    x=x+1
                self.type_keys_with_interval(1,'te12!@')
                if not self.find( "gravar_movimentofci", matching=0.97, waiting_time=10000):
                    self.not_found("gravar_movimentofci")
                self.click()
                if not self.find( "cancelar_movimentoFCI", matching=0.97, waiting_time=10000):
                    self.not_found("cancelar_movimentoFCI")
                self.click()
            
                if not self.find( "deletar_ir_movimentofci", matching=0.97, waiting_time=10000):
                    self.not_found("deletar_ir_movimentofci")
                self.click_relative(13, 358)
                self.enter()
                if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                    self.not_found("retornarfim")
                self.click()
                if not self.find( "fechargestaoadm", matching=0.97, waiting_time=10000):
                    self.not_found("fechargestaoadm")
                self.click()
                if not self.find( "simfecharfim", matching=0.97, waiting_time=10000):
                    self.not_found("simfecharfim")
                self.click()
                #self.enter()


def not_found(label) :
    print(f"Element not found  {label}")
    
if __name__ == '__main__' :
    Bot.main()  