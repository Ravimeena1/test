head=int(input("enter head"))
leg=int(input("enter leg"))
rabit=4
chicken=2
rabit_more_leg=rabit-chicken
leg=leg-head*2
rabit_head=leg//rabit_more_leg
chicken_head=head-rabit_head
print(rabit_head, chicken_head)
