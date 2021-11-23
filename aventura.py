
class jogo:
	def _init_(self):
			self.Iniciar='Você é um(a) soldado(a) que esta no meio de uma guerra ,seus aliados estão'
			self.pergunta1='Você escolhe dar apoio ou atacar?(1 apoiar/2 atacar)'
			self.resposta1a='va da suporte aos aliados'
			self.pergunta2='Você chega no campo de batalha e ve seus companheiros sendo derrotados um por um. O que você faz?'
			self.pergunta2a='curar ou resgatar(1 cura/ 2 resgata)'
			self.resposta2aA='voce curou seus aliados'
			self.pergunta3='Agora que seus companheiros voltaram a ação os inimigos sofrem com a ira deles. Mas vendo que eles estão em maior número vocês precisam de uma decisão rápida '
			self.pergunta3a='o que vocês decidem recuar ou avançar(1 recuar/2 avançar)'
			self.resposta3aA='vocês recuaram e trouxeram reforços , com isso venceram a batalha'
			self.resposta3aB='Eles aproveitaram a vantagem e atacaram todos ao mesmo tempo e você e toda sua compania morreram e só foram encontrados 10 dias depois já em decomposição.'
			self.reposta2aB='voce morrem tentando salvar os amigos'
			self.resposta1b='destrua os inimigos'
			self.pergunta2b='ao chegar na batalha você instintivamente avança para o combate, entretanto o que você faz(1 luta sozinho/2 lutar em grupo)'
			self.resposta2bA='você morre sem conseguir revidar'
			self.reposta2bB='com a força de seus companheiros , vocês começam a virar a batalha a seu favor'
			self.pegunta3b= 'com a btalha a seu favor você com um a decisão pode termina-la(1 fazer cerco/2 avançar com tudo)'  
			self.reposta3bA='com a tentaiva de fazer cerco, os inimigos se reagruparam acabando com seus aliados'
			self.reposta3bB='com o seu grande avanço os inimigos não conseguiram fazer uma decisão rapida, voce venceu'
			self.Venceu='Você venceu, parabens!!!!'        
			self.gameover='GAME OVER'
			self.resposta()


	def iniciar(self):

		print(self.Iniciar) 
		print(self.pergunta1)
		self.resposta()
		if self.resposta == '1':
					print(self.resposta1a)
					
					print(self.pergunta2)
				
					if self.resposta=='1':
						print(self.resposta2Aa)and print(self.pergunta3)
					if self.resposta =='2':
						print(self.resposta2aB)and print (self.gameover)	
					
						self.resposta()
						if self.resposta=='1':
							print(self.resposta3aA) and print(self.Venceu)
						if self.resposta=='2':
								print(self.resposta3aB) and print(self.gameover)
						if self.pergunta1=='2':
									print(self.resposta1b)
									print(self.pergunta2b)
									self.resposta()
									if self.resposta=='1':
										print(self.resposta2bA) and print(self.gameover) 
										if self.resposta=='2':
											print(self.resposta2bB)
											
											print(self.pergunta3b)
											self.resposta()
											if self.resposta=='1':
												print(self.reposta3bA) and print(self.gameover)
												if self.resposta=='2':
													print(self.reposta3bB) and print(self.Venceu)


jogo.iniciar()									
jogo = jogo()


			



            
		

		
	

   


