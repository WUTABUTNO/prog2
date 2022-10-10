#include <cstdlib>
#include <iostream>
// Person class 

class Person{
	public:
		Person(int);
		int fib();
		int get();
		void set(int);
	private:
		int age;
		int ffib(int);
};
 
Person::Person(int n){
	std::cout << "initializing" << std::endl;
	age = n;
	}

int Person::get(){
	return age;
	}

void Person::set(int n){
	age = n;
	}

int Person::ffib(int n) {
        if (n <= 1){
        return n;
        	}
        else{
                return ffib(n-1) + ffib(n-2);
        	}
	}

int Person::fib(){
	return ffib(age);
	}

extern "C"{
	Person* Person_new(int n) {return new Person(n);}
	int Person_get(Person* person) {return person->get();}
	void Person_set(Person* person, int n) {person->set(n);}
	int Person_fib(Person* person) {return person->fib();}
 	void Person_delete(Person* person){
		if (person){
			delete person;
			person = nullptr;
			}
		}
	}

