d = {"nome": "Ana", "idade": 30}
d = dict(nome="Ana", idade=30)
d = dict(zip(["a", "b"], [1, 2]))
d = dict.fromkeys(["a", "b"], 0)

d["nome"]                 # KeyError se não existir
d.get("email")            # None se não existir
d.get("email", "—")       # valor padrão
d["email"] = "a@x.com"    # adiciona/atualiza
d.setdefault("tags", [])  # define só se não existir
d.update({"idade": 31, "cidade": "SP"})
d |= {"pais": "BR"}       # merge in-place (3.9+)
novo = d | {"x": 1}       # merge novo dict

d.pop("idade")            # remove e retorna
d.pop("x", None)          # sem erro se não existir
d.popitem()               # remove o último inserido
del d["nome"]

d.keys(), d.values(), d.items()
"nome" in d               # verifica chave

for chave, valor in d.items():
    print(chave, valor)

# Ordenar por valor
sorted(d.items(), key=lambda kv: kv[1], reverse=True)

# Inverter chaves/valores
{v: k for k, v in d.items()}

from collections import defaultdict, Counter, OrderedDict, ChainMap

grupos = defaultdict(list)
grupos["frutas"].append("maçã")    # sem KeyError

c = Counter("abracadabra")
c.most_common(2)                   # [('a', 5), ('b', 2)]
c["z"]                             # 0
Counter(a=3) + Counter(a=1, b=2)