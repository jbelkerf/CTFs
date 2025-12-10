#include "../inc/dispatcher.hpp"

ws_logx& ws_logx::operator=(ws_logx x){
	if (this->logx_file.is_open()){
		this->logx_file.open(x.logx_path);
		this->logx_path = x.logx_path;
		this->logx_to_file = true;
	}else
		this->logx_to_file = false;
	this->logx_level = x.logx_level;
	return (*this);
}

ws_logx::ws_logx(std::string logx_path, std::string level){
	this->logx_path = logx_path;
	logx_level = detect_logx_level(level);
	if (logx_path.empty() == true || access(logx_path.c_str(), W_OK) == -1){
		logx_to_file = false;
		return;
	}
	logx_file.open(logx_path);
	logx_to_file = true;
}

ws_logx::~ws_logx(){
	logx_file.close();
}

void ws_logx::info(std::string msg){
	if (logx_level <= INFO){
		std::cout << "[" << BLUE << "*"  << DEFAULT << "] - " ;
		std::cout << msg << std::endl;
		if (logx_to_file == true){
			logx_file << msg << "\n" << std::flush;
		}
	}
}
void ws_logx::error(std::string msg){
	if (logx_level <= ERROR){
		std::cout << "[" << RED << "ERROR"  << DEFAULT << "] - " ;
		std::cout << msg << std::endl;
		if (logx_to_file == true){
			logx_file << msg << "\n" << std::flush;
		}
	}
}
void ws_logx::debug(std::string msg){
	if (logx_level <= DEBUG){
		std::cout << "[" << BLUE << "*"  << DEFAULT << "] - " ;
		std::cout << msg << std::endl;
		if (logx_to_file == true){
			logx_file << msg << "\n" << std::flush;
		}
	}
}
void ws_logx::warn(std::string msg){
	if (logx_level <= WARN){
		std::cout << "[" << YELLOW << "!"  << DEFAULT << "] - " ;
		std::cout << msg << std::endl;
		if (logx_to_file == true){
			logx_file << msg << "\n" << std::flush;
		}
	}
}

void ws_logx::set_logx_level(logx_LEVEL level){
	this->logx_level = level;
}

logx_LEVEL ws_logx::detect_logx_level(std::string &msg){
	if (msg == "ERROR")
		return (ERROR);
	if (msg == "WARN")
		return (WARN);
	if (msg == "INFO")
		return (INFO);
	if (msg == "DEBUG")
		return (DEBUG);
	return (NONE);
}
