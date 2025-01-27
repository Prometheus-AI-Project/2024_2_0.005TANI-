

def pitcher_model(pitcherHeight, pitchHand, pitchForm, lh_or_rh, strikes, balls, runners):
    
    
    #좌투/우투 피처 세팅
    if pitchHand =="좌투": #좌투가 0인지 1인지 확실하지 않음
        lp_or_rp=1
    else:
        lp_or_rp =0
    
    #투구 폼 세팅
    if pitchForm == "오버핸드":
        pitchform = 0
    elif pitchForm == "쓰리쿼터":
        pitchform = 1
    else:
        pitchform = 2
        

    #볼카운트 모델 피처 세팅
    more_strike = 0
    more_ball = 0
    same_strike_ball=0
    
    if strikes>balls:
        more_strike=1
    elif strikes<balls:
        more_ball=1
    else:
        same_strike_ball=1
    
    #주자 유뮤 모델 피처
    is_runner = 0
    no_runner = 0
    if runners>0:
        is_runner=1
    else:
        no_runner = 1
    
    #상대 타자 좌우타 모델 피처 세팅

    lh = 0
    rh = 0
    
    if lh_or_rh =="Right":
        rh=1
    else :
        lh = 1
    

    
    results_1 = pitch_ballcount_model(pitcherHeight, lp_or_rp, pitchform, more_strike, more_ball, same_strike_ball)
        


    results_2 = pitch_runner_model(pitcherHeight, lp_or_rp, pitchform, is_runner, no_runner)
        
        
    results_3 = pitch_lh_or_rh_model(pitcherHeight, lp_or_rp, pitchform, lh, rh)
    
    

    #model inference
    
    results = {}
    
    return results
    
    

    

def hitter_model(hiiter_height, pitchType, lp_or_rp, lh_or_rh, pitch_mechanic, strike, ball, runner):
    more_strike = 0
    more_ball = 0
    same_strike_ball=0
    
    if strike>ball:
        more_strike=1
    elif strike<ball:
        more_ball=1
    else:
        same_strike_ball=1
    
    is_runner = 0
    no_runner = 0
    if runner>0:
        is_runner=1
    else:
        no_runner = 1
    
    #상대 타자 좌우타 모델 피처 세팅

    lh = 0
    rh = 0
    
    if lh_or_rh =="Right":
        rh=1
    else :
        lh = 1
    
    results_1 =  hitter_ballcount_model(hitter_height, lh_or_rh, more_strike, more_ball, same_strike_ball)


    results_2 =  hitter_runner_model(hitter_height, lh_or_rh,  is_runner, no_runner)
        
    results_3 =  hitter_lp_or_rp_model(hitter_height, lh_or_rh, pitcher_form, lp, rp)
    
    results_4 =  hitter_pitchtype_model(hitter_height, lh_or_rh, pitch_type)
    
    
    results = {}
    
    return results
    



def pitch_ballcount_model(pitcher_height, lp_or_rp, pitcher_form, more_strike, more_ball, same_strike_ball):
    #inference 수행
    return 0


def pitch_runner_model(pitcher_height, lp_or_rp, pitcher_form, is_runner, no_runner):
    #inference 수행
    return 0
    
def pitch_lh_or_rh_model(pitcher_height, lp_or_rp, pitcher_form, lh, rh):
    #inference 수행
    return 0
    



def hitter_ballcount_model(hitter_height, lh_or_rh, more_strike, more_ball, same_strike_ball):
    #inference 수행
    return 0


def hitter_runner_model(hitter_height, lh_or_rh,  is_runner, no_runner):
    #inference 수행
    return 0
    
def hitter_lp_or_rp_model(hitter_height, lh_or_rh, pitcher_form, lp, rp):
    #inference 수행
    return 0

def hitter_pitchtype_model(hitter_height, lh_or_rh, pitch_type):
    #inference 수행
    return 0