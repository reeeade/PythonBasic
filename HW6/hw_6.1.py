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
        # Схема амортизации для для просчета ежемесячного вноса средств для закрытия кредита до конца указанного срока
        install = calc_proc / (1 - (1 + proc) ** (-months + month - 1))
        new_sum -= install
        print(f'{month:^10}{install:^45.2f}{calc_proc:^19.2f}')
