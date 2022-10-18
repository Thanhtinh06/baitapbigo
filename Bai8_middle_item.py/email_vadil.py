def check_email_vadil(n):
    domain = [46]
    local = [95, 46]
    upper_char = [i for i in range(65, 91)]
    lower_char = [j for j in range(97, 123)]
    digits = [i for i in range(48, 58)]
    rule_domain = domain + upper_char + lower_char
    rule_local = local + upper_char + lower_char + digits
    symbol = '@'
    symbol_index = n.find(symbol)
    count = 0
    for i in range(len(n)):
        if n[i] == symbol:
            count += 1
    if count > 1:
        return False
    else:
        email = n.strip()
        str_local_host = email[:symbol_index]
        str_domain = email[symbol_index+1:]

        # Local
        if len(str_local_host) < 1:
            return False

        for j in range(len(str_local_host)):
            if ord(str_local_host[j]) not in rule_local:
                return False

        # Domain

        s = '.'
        if str_domain.find(s) == -1 or len(str_domain) < 1:
            return False

        for k in range(len(str_domain)):
            if ord(str_domain[k]) not in rule_domain:
                return False
            if ord(str_domain[k]) == 46 and ord(str_domain[k-1]) == 46:
                return False

    return True


n = input()
result = check_email_vadil(n)
if result:
    print('VALID')
else:
    print('INVALID')
