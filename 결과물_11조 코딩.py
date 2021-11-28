ssum=0
ans='y'

print("===============")
print("1. 삼겹살 9000원")
print("2. 목살 9500원")
print("3. 껍데기 5000원")
print("===============")

while ans=='y' :
   chdr=int(input("어떤 고기를 드시겠습니까? 번호선택 : "))
   if chdr == 1:
      drco=int(input("몇 인분을 드릴까요?"))
      print("삼겹살을", drco, "인분 주문하셨고, 금액은", drco*9000,"원 입니다.")
      ssum=ssum+(drco*9000)

   elif chdr == 2:
      drco=int(input("몇 인분을 드릴까요?"))
      print("목살을", drco, "인분 주문하셨고, 금액은", drco*9500,"원 입니다.")
      ssum=ssum+(drco*9500)

   elif chdr == 3:
      drco=int(input("몇 인분을 드릴까요?"))
      print("껍데기를", drco, "인분 주문하셨고, 금액은", drco*5000,"원 입니다.")
      ssum=ssum+(drco*5000)

   else:
      print("잘못 누르셨습니다.")

   ans=input("다른 고기를 주문할까요?")

print("총 금액은", ssum, "원입니다,")

print('나눠서 계산 하시겠습니까?')

answ=input('예, 아니오: ')

if answ == '예':
   num=int(input(' 몇 명인지 적어주세요:'))
   print("각자", ssum/num, "원 입니다.")
else:
    print('결제를 진행하겠습니다.')

print("====================")
print('♧저희 매장을 방문해주셔서 감사합니다. 행복한 하루 보내세요.♧')


       

