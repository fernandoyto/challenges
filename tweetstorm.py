import math

def tweetstorm(text: str) -> list:
    n = len(text)
    if n <= 140:
        return text
    results = []
    init_tt_count = math.ceil(n / 140)
    if init_tt_count >= 10:
        extra_space = 9 * 5 # for tweets as x/xx
        extra_space += (init_tt_count - 9) * 6 # for tweets as xx/xx
    else:
        extra_space = 4 * init_tt_count

    final_tt_count = math.ceil((n + init_tt_count * extra_space) / 140)
    start_idx = 0
    for i in range(final_tt_count):
        curr_str = str(i + 1) + '/' + str(final_tt_count) + ' '
        for j in range(start_idx, n):
            if len(curr_str) < 140:
                curr_str += text[j]
                start_idx += 1
            else:
                results.append(curr_str)
                break
    results.append(curr_str)
    print(results)

tweetstorm('vamos ver se vai dar certo! esse aqui será meu primeiro tweet para testar. 140 caracteres parece pouco, mas qdo preciso lorotar é foda. lorotar é bem mais dificil do que parece! será que eu pensava dessa forma quando estava fazendo o tcc? kkkkk pq lá eu lorotei pra caralho! bons tempos. naquelas né. mas o assunto que eu estava estudando era de fato interessante. poderia ter continuado estudando, mas não sei se era bem o meu perfil')