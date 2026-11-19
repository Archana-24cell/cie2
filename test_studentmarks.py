from studentmarks import calculate_result

def test_total():
    total,average,percentage = calculate_result(80,90,70)

    assert total == 240
    assert average == 80
    assert percentage == 80

    def test_average():
        total,average,percentage = calculate_result(70,30,50)

        assert total == 150
        assert average == 50
        assert percentage == 50

        def test_percentage():
            total,average,percentage = calculate_result(70,60,90)
            
            assert total == 220
            assert average == 73
            assert percentage == 73
