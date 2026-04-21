import { Link } from "react-router-dom";
function Footer() {
    return (
      <div className="w-[full] h-[345px] bg-[#EEF2FF] ">
        <section className="grid grid-cols-[1fr_1fr_1fr_1fr] w-full h-[132px] gap-[48px] p-[32px] pt-[64px]">
          <div className="grid grid-rows-[2] gap-[14.75px] ">
            <p className="text-[18px] leading-[28px]  text-[#312E81]">
              Architect Elite
            </p>
            <p className="w-[268px] h-[69px] text-[14px] leading-[22.75px]  text-[#312E81B2]">
              Curating the finest digital and physical goods with architectural
              precision since 2024.
            </p>
          </div>
          <div className="grid grid-rows-[0.8fr_1.2fr] gap-[14.75px]">
            <p className="text-[18px] leading-[28px]  text-[#312E81]">
              Platform
            </p>
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
          <div className="grid grid-rows-[0.8fr_1.2fr] gap-[14.75px]">
            <p className="text-[18px] leading-[28px]  text-[#312E81]">
              Company
            </p>
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
          
        </section>
      </div>
    );
}
export default Footer;