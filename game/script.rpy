# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
image nariyeon = "nariyeon_logo.png"
image kasumi = "kasumi.png"
image bgStar = "bg.jpg" 

image bg1 = "bg1.png" 

image bg2 = "bg2.png" 
# 게임에서 사용할 캐릭터를 정의합니다.
define e = Character('토야마 카스미', color="#c8ffc8")

define utaha = Character('카스미가카\n우타하', color="#c8ffff")


# 여기에서부터 게임이 시작합니다.
label splashscreen:
    scene black 
    scene nariyeon with dissolve
    with Pause(1)
    scene black with dissolve
    return

label start:
    scene bgStar
    show kasumi
    e "별의 고동을 찾아서! 두구두구두구 여기에 맛좋은 별 고동이 있다며요??"
    e "안드로이드 스크립트 테스트용 입니다. 죽는 날까지 하늘을 우러러 한점 부끄럼이 없기를 잎새에 이는 바람에도 나는 괴로와했다 별을 노래하는 마음으로 모든 죽어가는 것들을 사랑해야지 그리고 나한테 주어진 길을 걸어가야겠다."
    
   
    
    scene bg1
    show kasumi
    e "별의 고동을 찾아서! 두구두구두구 여기에 맛좋은 별 고동이 있다며요??"
    e "이야기와 그림, 음악을 더하면 여러분dkfjhkjh kahkdslhf khakdsakjfhjkld sahfkhsda kljfhkjdsa hfjkhsdajklf hads lkjfhhehfklh ekwhfajkhj shjfk hasdj klf hj kld sah jfklh adsjlkfhjadskl의 게임을 세상에 배포할 수 있어요!"
    jump hell  
    return
label hell:
    scene bg2
    show kasumi
    utaha "별의 고동을 찾아서! 두구두구두구 여기에 맛좋은 별 고동이 있다며요??"
    utaha "이야기와 그림, 음악을 더하면 여러분dkfjhkjh kahkdslhf khakdsakjfhjkld sahfkhsda kljfhkjdsa hfjkhsdajklf hads lkjfhhehfklh ekwhfajkhj shjfk hasdj klf hj kld sah jfklh adsjlkfhjadskl의 게임을 세상에 배포할 수 있어요!"


