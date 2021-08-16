int getSum(int a, int b){
    unsigned int sum_excluding_carries = a ^ b;
    unsigned int carry = (a & b & 0xffffffff) << 1;
    unsigned int new_carry;

    while(carry != 0){
        new_carry = sum_excluding_carries & carry;
        sum_excluding_carries = sum_excluding_carries ^ carry;
        carry = (new_carry & 0xffffffff) << 1;
    }

    return sum_excluding_carries;
}