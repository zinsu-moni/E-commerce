import chair from "../assets/chair.png";
import Google from "..//assets/Google.png";
import Apple from "..//assets/Apple.png";
import Background from "..//assets/Background.png";
import { Link } from "react-router-dom";
function Login() {
  return (
    <div>
      <div className="flex flex-row w-full h-[876.5px]">
        {/* LEFT HAND SIDE  */}
        <div className="w-[1200px]">
          <img src={chair} alt="Chair" className="w-full h-full object-cover" />
        </div>
        {/* RIGHT HAND SIDE  */}
        <div className="flex-1 flex flex-col p-[96px] bg-[#FAF8FF]">
          <div className="pb-[10px]">
            <img
              src={Background}
              alt=""
              className=" w-[48px] h-[42px] object-cover  "
            />
          </div>
          <p className=" w-[320px] h-[36px]  text-[30px] leading-[36px] pt-[16px] tracking-[-0.75px] text-[#131B2E]">
            Welcome Back
          </p>
          <p className="text-[16px] leading-[24px] pt-[25px] text-[#434656]">
            Please enter your details to sign in.
          </p>
          <section className="mt-[45px]">
            <label
              htmlFor="email"
              className="font-semibold text-[14px] leading-[20px] tracking-[0.35px] text-[#434656] flex pb-[10px] "
            >
              EMAIL ADDRESS
            </label>{" "}
            <input
              type="email"
              placeholder="name@company.com"
              id="email"
              className="w-[320px] h-[49px] border border-[#C4C5D933] rounded-[8px] bg-[#FFFFFF] pl-[10px] "
            />
          </section>
          <section className="mt-[20px]">
            <label
              htmlFor="password"
              className="font-semibold text-[14px] leading-[20px] tracking-[0.35px] text-[#434656] flex flex-row justify-between py-[10px]"
            >
              PASSWORD
              <Link
                to="/"
                className="font-bold text-[14px] text-[#3132ED] leading-[20px]"
              >
                Forgot Password?
              </Link>
            </label>{" "}
            <input
              type="password"
              id="password"
              className="w-[320px] h-[49px] border border-[#C4C5D933] rounded-[8px] bg-[#FFFFFF] pl-[10px] "
            />
          </section>
          <div className="flex items-center gap-2 pt-[20px]">
            <input
              type="checkbox"
              id="keep-signed-in"
              className="w-[20px] h-[20px] border border-[#C4C5D933] rounded-[4px] accent-[#3132ED]"
            />
            <label
              htmlFor="keep-signed-in"
              className="text-[14px] text-[#434656]"
            >
              Keep me signed in
            </label>
          </div>
          <section>
            <button className="bg-[#3132ED] py-[12px] px-[24px] rounded-[8px] font-bold text-[14px] leading-[20px] w-[320px] h-[60px] mt-[30px]  shadow-[0px_4px_6px_-4px_#3132ED33,0px_10px_15px_-3px_#3132ED33] cursor-pointer hover:bg-[#131B2E] transition duration-300">
              <Link to="/dashboard">
                <p className="text-[#FFFFFF] font-bold leading-[28px] text-[18px] ">
                  {" "}
                  Sign In
                </p>
              </Link>
            </button>
          </section>
          <div className="flex items-center gap-3 w-full py-[32px] ">
            <div className="flex-1 h-[1px] bg-gray-300"></div>
            <p className="text-[#434656] text-[12px] font-medium tracking-[1.2px] leading-[16px] ">
              OR CONTINUE WITH
            </p>
            <div className="flex-1 h-[1px] bg-gray-300"></div>
          </div>
          <section className="flex  flex-row">
            <button className="w-[152px] h-[52px] bg-[#F2F3FF] rounded-[8px] flex items-center justify-center mr-[16px] cursor-pointer hover:bg-[#E0E1FF] transition duration-300">
              <Link to="/google-login" className="flex flex-row gap-2">
                <img src={Google} alt="Google" />
                <p className="font-bold text-[#131B2E] text-[14px] leading-[20px] ">
                  Google
                </p>
              </Link>
            </button>
            <button className="w-[152px] h-[52px] bg-[#F2F3FF] rounded-[8px] flex items-center justify-center cursor-pointer hover:bg-[#E0E1FF] transition duration-300">
              <Link to="/apple-login" className="flex items-center gap-2">
                <img
                  src={Apple}
                  alt="Apple"
                  className="w-[13.333333015441895px] h-[8.333333015441895px]"
                />
                <p className="font-bold text-[#131B2E] text-[14px] leading-[20px] ">
                  Apple
                </p>
              </Link>
            </button>
          </section>
          <div className="flex flex-row gap-[4px] mt-[32px]">
            <p className="font-medium text-[16px] leading-[24px] text-[#434656] ">
              New to the collective?{" "}
            </p>
            <Link
              to="/signup"
              className="font-bold text-[#3132ED] leading-[24px] text-[16px] "
            >
              Create an account
            </Link>
          </div>
        </div>
      </div>
      {/* FOOTER */}
      <footer className="h-[119px] bg-[#F2F3FF] flex flex-row justify-between w-full item-center p-[32px]">
        <div className="flex flex-col gap-[12px]">
          <p className="font-bold text-[18px] leading-[28px] tracking[-0.9px] text-[#4338CA] ">
            The Fluid Architect
          </p>
          <p className="text-[#64748B] leading-[22.75px] text-[14px] ">
            © 2024 The Fluid Architect. Secure SSL Encrypted.
          </p>
        </div>
        <div className="flex flex-row gap-[12px] items-center">
          <Link >
            <p className="text-[#64748B] leading-[22.75px] text-[14px] ">
              Privacy Policy
            </p>
          </Link>
          <Link>
            <p className="text-[#64748B] leading-[22.75px] text-[14px] ">
              Terms of Service
            </p>
          </Link>
          <Link>
            <p className="text-[#64748B] leading-[22.75px] text-[14px] ">
                Security Architecture
            </p>
          </Link>
        </div>
      </footer>
    </div>
  );
}
export default Login;
