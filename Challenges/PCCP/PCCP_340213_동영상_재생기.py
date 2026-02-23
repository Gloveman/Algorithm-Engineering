"""
초 단위로 연산하자.
10초 전, 10초 뒤, 오프닝 건너뛰기
오프닝 건너뛰기의 경우 지금 구간이 오프닝에 해당하면 알아서 건너뜀

초 단위로 통일한 점, 처음 pos의 범위도 체크한 점, min과 max를 이용해 비디오 처음 혹은 마지막으로 이동하는 조건을 잘 처리
개선점
- 처음에 변환하는 부분의 코드가 중복되므로, 이를 별도 함수로 빼는 것이 좋음(오프닝 확인도 마찬가지)
- result_m이나 result_s가 정확히 10인 경우에 대해 잘못 계산될 수 있음(처음에 >=를 쓰지 않았음)
- 0을 추가해 2자리로 맞추는 것은 str(num).zfill(2)로 가능하다

"""
def solution(video_len, pos, op_start, op_end, commands):
    video_end_s= int(video_len[:2]) * 60 + int(video_len[3:])
    op_start_s = int(op_start[:2]) * 60 + int(op_start[3:])
    op_end_s = int(op_end[:2]) * 60 + int(op_end[3:])
    cur_pos_s = int(pos[:2]) * 60 + int(pos[3:])
    #처음부터 오프닝에 있는 경우
    if op_start_s <= cur_pos_s <=op_end_s:
        cur_pos_s = op_end_s
    for cmd in commands:
        # 커멘드 실행
        if cmd == 'prev':
            cur_pos_s = max(0, cur_pos_s - 10)
        else:
            cur_pos_s = min(video_end_s, cur_pos_s + 10)
            
        # 오프닝에 있는지 확인
        if op_start_s <= cur_pos_s <=op_end_s:
            cur_pos_s = op_end_s
    
    result_m = cur_pos_s // 60
    result_s = cur_pos_s % 60
    result_m = str(result_m) if result_m >= 10 else "0"+str(result_m)
    result_s = str(result_s) if result_s >= 10 else "0"+str(result_s)
    return ":".join([result_m, result_s])