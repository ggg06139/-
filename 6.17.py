#6.17 182526 황승현

population_A = (100, 150, 230, 120, 180, 100, 140, 95, 81, 21, 4)
population_B = (300, 420, 530, 420, 400, 300, 40, 5, 1, 1, 1)

print(f'마을 A와 B에 보낼 투표용지의 개수는 각각 {sum(population_A[2:])} 장과 {sum(population_B[2:])} 장 입니다.')
print(f'마을 A와 B의 고령화 정도는 각각 {round(sum(population_A[7:])/sum(population_A),3)}와 {round(sum(population_B[7:])/sum(population_B),3)}입니다.')
