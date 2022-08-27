# 마린 : 공격 유닛, 군인. 총을 쏠 수 있음
#name = "마린" # 유닛의 이름
#hp = 40 # 유닛의 체력
#damage = 5  # 유닛의 공격력

#print("{0} 유닛이 생성되었습니다.".format(name))
#print("체력은 {0}, 공격력 {1}\n".format(hp, damage))

# 탱크 : 공격 유닛, 탱크. 포를 쏠 수 있는데, 일반 모드 / 시즈모드.
#tank_name = "탱크"
#tank_hp = 150
#tank_damage = 35

#print("{0} 유닛이 생성되었습니다.".format(tank_name))
#print("체력은 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

#tank2_name = "탱크"
#tank2_hp = 150
#tank2_damage = 35

#print("{0} 유닛이 생성되었습니다.".format(tank2_name))
#print("체력은 {0}, 공격력 {1}\n".format(tank2_hp, tank2_damage))

#def attack(name, location, damage):
  #  print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format( \
 #       name, location, damage))
    
#attack(name, "1시", damage)
#attack(tank_name, "1시", tank_damage)

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{ 유닛 생성".format(name))
        
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))
        
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))
# 공격 유닛        
class AttackUnit(Unit):
    def __init__(self, name, hp, damage, speed):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.speed = speed
        
    #def attack(self, location):
       # print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"\
      #      .format(self.name, location, self.damage))
     #   
    #def damaged(self, damage):
     #   print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
    #    self.hp -= damage
   #     print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
  #      if self.hp <= 0:
 #           print("{0} : 파괴되었습니다.".format(self.name))
 
 # 마린
class Marine(AttackUnit):
     def __init__(self):
         AttackUnit.__init__(self, "마린", 40, 5, 1)
         
     # 스팀팩 : 일정 시간 동안 이동 및 공격 속도를 증가, 체력 10 감소
     def stimpack(self):
         if self.hp > 10:
             self.hp -= 10
             print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
         else:
             print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))
             
             
# 탱크
class Tank (AttackUnit):
    # 시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능. 이동 불가.
    seize_developed = False # 시즈 모드 개발여부
    
    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 35, 1)
        self.seize_mode = False
        
    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return
        
        # 현재 시즈 모드가 아닐 때 -> 시즈모드
        if self.seize_mode == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        # 현재 시즈모드일 때 -> 시즈모드 해제
        else:
            print("{0} : 시즈모드를 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False
            
        
        
        
        
    
    


# 날 수 있는 기능을 가진 클래스
class Flyable:
        def __init__(self, flying_speed):
           self.flying_speed = flying_speed  
        
        def fly(self, name, location):
            print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
                .format(name, location, self.flying_speed))
        
# 공중 공격 유닛 클래스
class FlyableAttackUnit(Flyable, AttackUnit):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0
        Flyable.__init__(self, flying_speed)
        
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 레이스
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit("레이스", 80, 20, 5)
        self.clocked = False # 클로킹 모드 (해제 상태)
        
    def clocking(self):
        if self.clocked == True: # 클로킹 모드 -> 모드 해제
            print("{0} : 클로킹 모드를 해제합니다.".format(self.name))
            self.clocked = False
        else: # 클로킹 모드 해제 -> 모드 설정
            print("{0} : 클로킹 모드로 설정합니다.".format(self.name))
            self.clocked = True