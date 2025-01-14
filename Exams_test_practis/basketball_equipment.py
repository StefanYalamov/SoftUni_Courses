SNEAKERS = 0.40
TEAM = 0.20
BALL = 0.25
OTHERS = 0.20

yearly_tax = int(input())

sneakers_price = yearly_tax - (yearly_tax * SNEAKERS)
team_price = sneakers_price - (sneakers_price * TEAM)
ball_price = team_price * BALL
others_price = ball_price * OTHERS
total = yearly_tax + sneakers_price + team_price + ball_price + others_price

print(f"{total:.2f}")
