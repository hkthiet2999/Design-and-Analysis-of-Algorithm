def DefAcceptance(boys_favl, girls_favl):

    couple_n = len(boys_favl)
    loved_list = [-1] * couple_n
    single_boy = [i for i in range(couple_n)]

    fav_ranking_list = [[0]*couple_n]*couple_n

    for i in range(couple_n):
        for j in range(couple_n):
            fav_ranking_list[i][girls_favl[i][j]] = j
    while single_boy:
        boy = single_boy[0]
        girl = boys_favl[boy].pop(0)

        if loved_list[girl] == -1:
            loved_list[girl] = boy
            single_boy.pop(0)

        else:
            if fav_ranking_list[girl][boy] < fav_ranking_list[girl][loved_list[girl]]:
                single_boy.pop(0)
                single_boy.append(loved_list[girl])
                loved_list[girl] = boy

    couples = [(loved_list[i], i) for i in range(couple_n)]

    return couples

def main():
    boys_favl = [[1,0,2,3],
                [3,0,1,2],
                [0,2,1,3],
                [1,2,0,3]]
    girls_favl = [[0,2,1,3],
                [2,3,0,1],
                [3,1,2,0],
                [2,1,0,3]]

    couples = DefAcceptance(boys_favl, girls_favl)
    print("Boy | Girl")
    for i in range(len(couples)):
        print(couples[i][0], end="   | ")
        print(couples[i][1])

main()