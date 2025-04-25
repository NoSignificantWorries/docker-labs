#include <cstdlib>
#include <iostream>

int main(int argc, char* argv[]){
	std::cout << "Hello two stage build!" << std::endl;
	for(int i=1; i < argc; i++){
		std::cout << "Argument " << i << ": ";
		std::cout << argv[i] << std::endl;
	}
	std::cout << "Environment:" << std::endl;
	if (argc >= 2){
		const char* envv_name = argv[1];
		const char* envv_value = std::getenv(envv_name);
		if(envv_value != nullptr){
			std::cout << envv_name << " = " << envv_value << std::endl;
		}
		else{
			std::cout << envv_name << " not found!" << std::endl;
		}
	}
	else{
		std::cout << "Not enough arguments to read evironment variable name" << std::endl;
	}
	return 0;
}

