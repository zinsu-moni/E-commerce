import { Link } from "react-router-dom";
import logBG from "../assets/logBG.png";
import Google from "..//assets/Google.png";
import Apple from "..//assets/Apple.png";
const Signup = () => {
  return (
    <div className="flex min-h-screen">
      {/* LEFT HAND SIDE */}
      <section className="w-1/2">
        <Link>
          <img src={logBG} alt="Logo" className="w-full h-full object-cover" />
        </Link>
      </section>
      {/* RIGHT HAND SIDE */}
      <section className="w-1/2 flex flex-col p-[80px] bg-[#FAF8FF]">
        <p className="font-black text-[#4338CA] tracking-[-1.2px] leading-[32px] text-[24px] font-Inter pb-[32px]">
          The Fluid Architect
        </p>
        <p className="tracking-[-1.2px] leading-[36px] text-[#131B2E] text-[30px]">
          Create Account
        </p>
        <p className="text-[#434656] text-[16px] leading-[24px] pt-[14px] pb-[32px]">
          Enter your details to start your journey.
        </p>
        <div className="mb-[32px]">
          <label
            htmlFor="fullname"
            className="font-semibold text-[14px] leading-[20px] tracking-[0.35px] text-[#434656] flex pb-[5px]"
          >
            FULL NAME
          </label>
          <input
            type="text"
            placeholder="Alexander Fluid"
            id="fullname"
            className="w-[448px] h-[55px] border border-[#C4C5D933] rounded-[8px] bg-[#FFFFFF] pl-[10px] "
          />
        </div>
        <section className="mb-[32px]">
          <label
            htmlFor="email"
            className="font-semibold text-[14px] leading-[20px] tracking-[0.35px] text-[#434656] flex pb-[5px]"
          >
            EMAIL ADDRESS
          </label>
          <input
            type="email"
            placeholder="alexander.fluid@example.com"
            id="email"
            className="w-[448px] h-[55px] border border-[#C4C5D933] rounded-[8px] bg-[#FFFFFF] pl-[10px] "
          />
        </section>
        <div className="flex flex-row gap-[16px] ">
          <div>
            <label
              htmlFor="password"
              className="font-semibold text-[14px] leading-[20px] tracking-[0.35px] text-[#434656] flex pb-[5px]"
            >
              PASSWORD
            </label>
            <input
              type="password"
              id="password"
              className="w-[216px] h-[55px] border border-[#C4C5D933] rounded-[8px] bg-[#FFFFFF]"
            />
          </div>
          <div>
            <label
              htmlFor="confirmPassword"
              className="font-semibold text-[14px] leading-[20px] tracking-[0.35px] text-[#434656] flex pb-[5px]"
            >
              CONFIRM PASSWORD
            </label>
            <input
              type="password"
              id="confirmPassword"
              className="w-[216px] h-[55px] border border-[#C4C5D933] rounded-[8px] bg-[#FFFFFF]"
            />
          </div>
        </div>
        <section className="flex item-center gap-[12px] pt-[32px]">
          <input
            type="checkbox"
            id="terms-cond"
            className="w-[20px] h-[20px] rounded-[4px] bg-[#FFFFFF] border border-[#C4C5D94D] accent-[#3132ED]"
          />
          <label htmlFor="terms-cond" className="text-[14px] text-[#434656]">
            I agree to the{" "}
            <Link to="/terms" className="font-bold text-[#3132ED]">
              <span> Terms of Service </span>
            </Link>
            and{" "}
            <Link to="/privacy" className="font-bold text-[#3132ED]">
              <span> Privacy Architecture </span>
            </Link>
          </label>
        </section>
        <div className="flex mt-[32px]">
          <button className="bg-gradient-to-r from-[#3132ED] to-[#5054FF] py-[12px] px-[24px] rounded-[8px] font-bold text-[14px] leading-[20px] w-[448px] h-[60px] mt-[30px]  shadow-[0px_4px_6px_-4px_#3132ED33,0px_10px_15px_-3px_#3132ED33] cursor-pointer hover:bg-[#131B2E] transition duration-300">
            <Link to="/dashboard">
              <p className="text-[#FFFFFF] font-bold leading-[28px] text-[18px] ">
                {" "}
                CREATE ACCOUNT
              </p>
            </Link>
          </button>
        </div>
        <div className="flex flex-row  mt-[32px] gap-[16px] items-center">
          <div className="w-[155.75px] h-[1px] bg-[#C4C5D933] "></div>
          <p className="font-bold text-[#747688] text-[12px] leading-[16px] tracking-[-0.6px]">
            OR REGISTER WITH
          </p>
          <div className="w-[155.75px] h-[1px] bg-[#C4C5D933] "></div>
        </div>
        <section className="flex  flex-row mt-[32px]  items-center">
          <button className="w-[211.47999572753906px] h-[46px] bg-[#F2F3FF] rounded-[8px] flex items-center justify-center mr-[16px] cursor-pointer hover:bg-[#E0E1FF] transition duration-300">
            <Link to="/google-login" className="flex flex-row gap-2">
              <img src={Google} alt="Google" />
              <p className="font-bold text-[#131B2E] text-[14px] leading-[20px] ">
                Google
              </p>
            </Link>
          </button>
          <button className="w-[211.47999572753906px] h-[46px] bg-[#F2F3FF] rounded-[8px] flex items-center justify-center cursor-pointer hover:bg-[#E0E1FF] transition duration-300">
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
        <div className="flex flex-row gap-[4px] mt-[32px] justify-center items-center w-[448px]">
          <p className=" text-[14px] leading-[20px] text-[#434656] ">
            Already an architect?{" "}
          </p>
          <Link
            to="/login"
            className="font-bold text-[#3132ED] leading-[24px] text-[16px] "
          >
            log in
          </Link>
        </div>
        <section className="flex flex-row gap-[24px] mt-[96px] justify-center items-center w-[448px]">
          <Link
            to="/help"
            className="font-bold leading-[16px] tracking-[1.2px] text-[12px] text-[#747688] uppercase"
          >
            Help
          </Link>
          <Link
            to="/privacy"
            className="font-bold leading-[16px] tracking-[1.2px] text-[12px] text-[#747688] uppercase"
          >
            Privacy
          </Link>
          <Link
            to="/conditions"
            className="font-bold leading-[16px] tracking-[1.2px] text-[12px] text-[#747688] uppercase"
          >
            Conditions
          </Link>
        </section>
        <p className="text-[10px] tracking-[2px] leading-[15px] text-[#747688] w-[448px] text-center mt-[24px]">
          © 2024 THE FLUID ARCHITECT. SECURE SSL ENCRYPTED.
        </p>
      </section>
    </div>
  );
};
export default Signup;
