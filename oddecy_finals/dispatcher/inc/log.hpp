#ifndef log_HPP
#define log_HPP

#include <fstream>
#include <unistd.h>
#include <fcntl.h>


#define RED "\033[0;31m"		// error
#define BLUE "\033[0;31m"		// debug/info
#define YELLOW "\033[0;33m"		// warning
#define DEFAULT "\033[0m"

typedef enum logx_LEVEL{
	ERROR,
	WARN,
	INFO,
	DEBUG,
	NONE
}logx_LEVEL;

class ws_logx{
	private :
		std::ofstream	logx_file;
		std::string	logx_path;
		logx_LEVEL	logx_level;
		bool		logx_to_file;
	public :
		ws_logx(std::string logx_path, std::string level);
		ws_logx(){};
		ws_logx& operator=(ws_logx x);
		~ws_logx();
		void info(std::string msg);
		void error(std::string msg);
		void debug(std::string msg);
		void warn(std::string msg);

		void set_logx_level(logx_LEVEL level);
		logx_LEVEL detect_logx_level(std::string &msg);
};

extern ws_logx logx;

#endif
