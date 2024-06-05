def YTM(R, F, P, n):
    C=F*R #1년간 이자지급액=액면가*이자율
    ytm=(C+(F-P)/n)/((F+P)/2)
    ytm=ytm*100 #%로 변환
    ytm=f"{ytm:.2f}%" #소수점 2자리까지만 출력& %붙이기
    print(ytm)
    return ytm
R=float(input("표면금리를 %로 입력해주세요"))/100
F=float(input("액면가를 입력해주세요"))
P=float(input("현재가를 입력해주세요"))
n=float(input("만기를 년도로 입력해주세요"))
YTM(R, F, P, n)
