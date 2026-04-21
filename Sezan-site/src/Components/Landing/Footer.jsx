import { Link } from "react-router-dom";
import Earth from "../../assets/Earth.png";
import Share from "../../assets/Share.png";
import Card from "../../assets/Card.png";
import Eye from "../../assets/Eye.png";
function Footer() {
  return (
    <div className="w-[full] h-[345px] bg-[#EEF2FF] flex flex-col justify-between">
      <section className="grid grid-cols-[1fr_1fr_1fr_1fr] w-full h-[132px] gap-[48px] p-[32px] pt-[64px]">
        <div className="flex flex-col gap-[14.75px]">
          <p className="text-[18px] leading-[28px]  text-[#312E81]">
            Architect Elite
          </p>
          <p className="w-[268px] text-[14px] leading-[22.75px]  text-[#312E81B2]">
            Curating the finest digital and physical goods with architectural
            precision since 2024.
          </p>
        </div>
        <div className="flex flex-col gap-[14.75px]">
          <p className="text-[18px] leading-[28px]  text-[#312E81]">Platform</p>
          <div className="grid grid-rows-[1fr_1fr_1fr_1fr] gap-[12px]">
            <Link to="/">
              <p className="text-[#312E81B2] text-[14px] leading-[20px] tracking-[0.35px]">
                Shop All
              </p>
            </Link>
            <Link to="/">
              <p className="text-[#312E81B2] text-[14px] leading-[20px] tracking-[0.35px]">
                COllections
              </p>
            </Link>
            <Link to="/">
              <p className="text-[#312E81B2] text-[14px] leading-[20px] tracking-[0.35px]">
                New Arrivals
              </p>
            </Link>
          </div>
        </div>
        <div className="flex flex-col gap-[14.75px]">
          <p className="text-[18px] leading-[28px]  text-[#312E81]">Company</p>
          <div className="grid grid-rows-[1fr_1fr_1fr_1fr] gap-[12px]">
            <Link to="/">
              <p className="text-[#312E81B2] text-[14px] leading-[20px] tracking-[0.35px]">
                Privacy Policy
              </p>
            </Link>
            <Link to="/">
              <p className="text-[#312E81B2] text-[14px] leading-[20px] tracking-[0.35px]">
                Terms of Service
              </p>
            </Link>
            <Link to="/">
              <p className="text-[#312E81B2] text-[14px] leading-[20px] tracking-[0.35px]">
                Shipping & Returns
              </p>
            </Link>
          </div>
        </div>
        <div className="flex flex-col gap-[14.75px]">
          <p className="text-[18px] leading-[28px]  text-[#312E81]">Support</p>
          <div className="grid grid-rows-[1fr_1fr_1fr_1fr] gap-[12px]">
            <Link to="/">
              <p className="text-[#312E81B2] text-[14px] leading-[20px] tracking-[0.35px]">
                Contact Us
              </p>
            </Link>
            <Link to="/">
              <p className="text-[#312E81B2] text-[14px] leading-[20px] tracking-[0.35px]">
                Help Center
              </p>
            </Link>
            <section className="flex flex-row  gap-[16px]">
              <img src={Earth} alt="Earth" />
              <img src={Share} alt="Share " />
            </section>
          </div>
        </div>
      </section>

      <section className="h-[53px]  flex flex-row justify-between px-[32px]">
        <p className="h-[20px] font-medium text-[14px] leading[20px] tracking-[0.35px] text-[#312E81B2]">
          © 2024 The Fluid Architect. All rights reserved.
        </p>
        <p className="flex flex-row gap-[23.99px]">
          <img src={Card} alt="Card" className="w-[22px] h-[16px] " />
          <img src={Eye} alt="Eye" className="w-[22px] h-[16px] " />
        </p>
      </section>
    </div>
  );
}
export default Footer;
