import os
import shutil

class LogChecker:
    default_dir = str(os.path.abspath(os.getcwd()))
    main_dir_check = False
    wallet_count = 0
    wallet_destination_dir = ""

    def __main__(self):
        self.log_run()

    def log_run(self):
        for dir in os.listdir():
            if os.path.isdir(dir):
                os.chdir(dir)
                for wallet_dir_find in os.listdir():
                    if str(wallet_dir_find) == "Wallets":
                        self.how_much_wallets_check(wallet_dir_find)
                        if self.wallet_count > 0:  # Only proceed if wallets are found
                            self.main_dir_check_method()
                            self.wallet_path_create()
                            shutil.copytree(
                                str(os.path.abspath(os.getcwd())),
                                f"{self.wallet_destination_dir}/{str(os.path.basename(os.getcwd()))}"
                            )
                        self.wallet_count = 0
                os.chdir(self.default_dir)

    def main_dir_check_method(self):
        if not self.main_dir_check:
            current_dir = str(os.path.abspath(os.getcwd()))
            os.chdir(self.default_dir)
            if os.path.exists("Холодные кошельки"):
                shutil.rmtree("Холодные кошельки")
            os.mkdir("Холодные кошельки")
            os.chdir(current_dir)
            self.main_dir_check = True

    def how_much_wallets_check(self, wallet_dir):
        self.wallet_count = len(os.listdir(wallet_dir))

    def wallet_path_create(self):
        current_dir = str(os.path.abspath(os.getcwd()))
        os.chdir(str(self.default_dir))
        os.chdir("Холодные кошельки")
        if not os.path.exists(str(self.wallet_count)):
            os.mkdir(str(self.wallet_count))
        os.chdir(str(self.wallet_count))
        self.wallet_destination_dir = str(os.path.abspath(os.getcwd()))
        os.chdir(current_dir)

print("Start")
Checks = LogChecker()
Checks.log_run()
print("End")
