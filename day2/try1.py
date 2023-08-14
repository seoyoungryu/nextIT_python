#예외처리 try~except
def test(values):
    sum = None
    try:
        sum = values[0]+values[1]+values[2]
    except IndexError as err: #index 에러만 ..
        print(str(err))
    except Exception as err: #어떤 오류라도 ..
        print(str(err))
    else:
        print('정상처리')
    finally:
        print('무조건 처리')
test([1,2,3])
test([1,2]) #인덱스 에러