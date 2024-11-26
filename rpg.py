from random import randint

lista_npc = []

player = {
   "nome": "Augusto",
   "level": 1,
   "exp": 0,
   "expMax": 50,
   "hp": 100,
   "hpMax": 100,
   "dano": 25
}

def create_mon(level):
    novoNpc = {
        "nome": f"Monstro @{level}",
        "level": level,
        "dano": 5 * level,
        "hp": 100 * level,
        "hpMax": 100 * level,
        "exp": 7*level,
    }
    return novoNpc

def createMonsters(n_npcs):
    for x in range(n_npcs):
     npc = create_mon(x + 1 )
    lista_npc.append(npc)

def exibir_npcs():
   for npc in lista_npc:
    print(
       f"Nome: {npc['nome']} // Level: {npc['level']} // Dano: {npc['dano']} // Vida: {npc['hp']}")

def reset_player():
   player['hp'] = player['hpMax']


def reset_npc(npc):
   npc['hp'] = npc['hpMax']


def Iniciar_batalha(npc):
   while player['hp'] > 0 and npc['hp'] > 0:
    atacar_npc(npc)
    atacar_player(npc)
    exibir_info_batalha(npc)
    if player['hp'] > 0:
       print(f"{player['nome']} venceu e ganhou {npc['exp']} de EXP\n")
       player['exp'] += npc['exp']
    else:
       print("O monstro venceu\n")

       reset_player()
       reset_npc(npc)



def atacar_npc(npc):
    npc['hp'] -= player['dano']




def atacar_player(npc):
    player['hp'] -= npc['dano']



def exibir_info_batalha(npc):
    print(f"Player HP:  {player['hp']}/{player['hpMax']} ")
    print(f"NPC: {npc['nome']}: {npc['hp']}/{npc['hpMax']} ")
    print("____________________________________________\n")


createMonsters(1)
  

npc_selecionado = lista_npc[0]
Iniciar_batalha(npc_selecionado)
