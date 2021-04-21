from All_home_works.hw2.task2 import major_and_minor_elem


def test_major_and_minor_elem_example1_from_description():
    input1 = [3, 2, 3]
    output1 = 3, 2
    assert output1 == major_and_minor_elem(input1)


def test_major_and_minor_elem_example2_from_description():
    input2 = [2, 2, 1, 1, 1, 2, 2]
    output2 = 2, 1
    assert output2 == major_and_minor_elem(input2)
