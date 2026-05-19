import chair from "../assets/chair.png";
import Google from "..//assets/Google.png";
import Apple from "..//assets/Apple.png";
import Background from "..//assets/Background.png";
import { Link } from "react-router-dom";
function Login() {
  return (
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
      </div>
    </div>
  );
}
export default Login;
