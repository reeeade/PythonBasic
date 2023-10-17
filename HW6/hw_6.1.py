sum_credit = int(input("Введите сумму кредита: "))
years = [1, 5]
for year in years:
    new_sum = sum_credit
    print(f'{"-" * 20}Помесячный план выплат на {year}год/лет{"-" * 20}')
    print(f'{"Месяц":^10}{"Сумма выплаты":^45}{"Насчитано процентов":^19}')
    months = year * 12
    for month in range(1, months + 1):
        if month <= 24:
            proc = 0.02
        else:
            proc = 0.04
        calc_proc = new_sum * proc
        install = sum_credit / months + calc_proc
        new_sum -= sum_credit / months
        print(f'{month:^10}{install:^45.2f}{calc_proc:^19.2f}')
