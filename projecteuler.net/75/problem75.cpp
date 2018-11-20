#include <iostream>
#include <cmath>
#include <chrono>
#include <thread>

const int L = 1500000;
int count = 0;
int w = 0;

void print_progress() {
	using namespace std::chrono_literals;
	while(1) { 
		std::cout << "\rw=" << w << " count=" << count;
		std::this_thread::sleep_for(2s);
	}
}

bool has_at_least_one_rat(int l) {
	for(int a = 1; a < l / 2; a++) {
		long int k = (std::pow(l, 2) - 2 * l * a);
		long int v = (2*l - 2*a);
		if (k % v == 0) {
			//int b = k / v;
			return true;
		}
	}
	return false;
}

int main() {
	std::thread t {print_progress};

	while(w <= L) {
		if (has_at_least_one_rat(w))
			count++;
		w++;
	}
}

/*
	~16:20 start 
    ~6min - w=276303 (138 000 in 3 min) count=234979
	~9 w=366595  (90 000 in 3 min)  count=325271
	16:32 412371  44 000 in 3 min
	 16:36 459244. 47 000 in 4 min
 */
