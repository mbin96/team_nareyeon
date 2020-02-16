# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.

image kasumi = "kasumi.png"
image bgStar = "bg.jpg" 

image bg1 = "bg1.png" 

image bg2 = "bg2.png" 
# 게임에서 사용할 캐릭터를 정의합니다.
define e = Character('토야마 카스미', color="#c8ffc8")

define utaha = Character('카스미가카\n우타하', color="#c8ffff")


# 여기에서부터 게임이 시작합니다.
label start:
    scene bgStar
    show kasumi
    e "별의 고동을 찾아서! 두구두구두구 여기에 맛좋은 별 고동이 있다며요??"
    e "이야기와 그림, 음악을 더하면 여러분 adsjlkfhjadskl의 게asffadsfads dfadffafasdfasdfads dafsadfadsffsd임을 세상에 배포할 수 있어요!"
    scene bg1
    show kasumi
    e "별의 고동을 찾아서! 두구두구두구 여기에 맛좋은 별 고동이 있다며요??"
    e "이야기와 그림, 음악을 더하면 여러분dkfjhkjh kahkdslhf khakdsakjfhjkld sahfkhsda kljfhkjdsa hfjkhsdajklf hads lkjfhhehfklh ekwhfajkhj shjfk hasdj klf hj kld sah jfklh adsjlkfhjadskl의 게임을 세상에 배포할 수 있어요!"
    scene bg2   
    show kasumi
    utaha "별의 고동을 찾아서! 두구두구두구 여기에 맛좋은 별 고동이 있다며요??"
    utaha "이야기와 그림, 음악을 더하면 여러분dkfjhkjh kahkdslhf khakdsakjfhjkld sahfkhsda kljfhkjdsa hfjkhsdajklf hads lkjfhhehfklh ekwhfajkhj shjfk hasdj klf hj kld sah jfklh adsjlkfhjadskl의 게임을 세상에 배포할 수 있어요!"
    
    
    return
