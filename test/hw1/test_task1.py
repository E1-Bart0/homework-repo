from All_home_works.hw1.task1 import check_fibonacci


def test_check_valid_data():
    data = (
        0,
        1,
        1,
        2,
        3,
        5,
        8,
        13,
        21,
        34,
        55,
        89,
        144,
        233,
        377,
        610,
        987,
        1597,
        2584,
        4181,
    )
    assert check_fibonacci(data)


def test_check_valid_data__not_from_begin():
    data = (
        832040,
        1346269,
        2178309,
        3524578,
        5702887,
        9227465,
        14930352,
        24157817,
        39088169,
        63245986,
        102334155,
        165580141,
        267914296,
        433494437,
        701408733,
        1134903170,
        1836311903,
        2971215073,
        4807526976,
        7778742049,
    )
    assert check_fibonacci(data)


def test_check_no_data():
    data = ()
    assert not check_fibonacci(data)


def test_check_invalid_data_first():
    data = (
        5,
        0,
        1,
        1,
        2,
        3,
        5,
        8,
        13,
        21,
        34,
        55,
        89,
        144,
        233,
        377,
        610,
        987,
        1597,
        2584,
        4181,
    )
    assert not check_fibonacci(data)


def test_check_invalid_data_last():
    data = (
        0,
        1,
        1,
        2,
        3,
        5,
        8,
        13,
        21,
        34,
        55,
        89,
        144,
        233,
        377,
        610,
        987,
        1597,
        2584,
        4181,
        1,
    )
    assert not check_fibonacci(data)


def test_check_invalid_data_middle():
    data = (
        0,
        1,
        1,
        2,
        3,
        5,
        8,
        13,
        21,
        34,
        55,
        89,
        100000,
        144,
        233,
        377,
        610,
        987,
        1597,
        2584,
        4181,
    )
    assert not check_fibonacci(data)


def test_check_invalid_data_not_from_begin():
    data = (
        37889062373143906,
        61305790721611591,
        99194853094755497,
        160500643816367088,
        259695496911122585,
        420196140727489673,
        679891637638612258,
        1100087778366101931,
        1779979416004714189,
        2880067194370816120,
        113804746346429,
        12200160415121876738,
        19740274219868223167,
        31940434634990099905,
        51680708854858323072,
        83621143489848422977,
        135301852344706746049,
        218922995834555169026,
        1,
    )
    assert not check_fibonacci(data)
