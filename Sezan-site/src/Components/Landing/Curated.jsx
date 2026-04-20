import { Link } from "react-router-dom";
import arrow2 from "../../assets/arrow2.png";
import Electronics from "../../assets/Electronics.png";
import Fashion from "../../assets/Fashion.png";
import Home from "../../assets/Home.png";
import Lifestyle from "../../assets/Lifestyle.png";
function Curated() {
  const images = [
    { id: 0, src: Electronics, alt: "Electronics" },
    { id: 1, src: Fashion, alt: "Fashion" },
    { id: 2, src: Home, alt: "Home" },
    { id: 3, src: Lifestyle, alt: "Lifestyle" },
  ];
  return (
    <div className="bg-[#F2F3FF]  size-auto ">
      <div className="flex flex-row items-center justify-between pt-[96px] pr-[32px] pb-[96px] pl-[32px]">
        <h1 className=" font-black text-[36px] text-[#312E81] leading-[40px] tracking-[0.9px]">
          Curated Collections
        </h1>
        <Link
          to="/login"
          className=" font-bold text-[16px] text-[#3132ED] leading-[24px] flex flex-row gap-[8px] h-[24px] "
        >
          View All Categories{" "}
          <img
            src={arrow2}
            alt="Arrow"
            className="object-cover w-[15px] h-[15px] cursor-pointer"
          />
        </Link>
      </div>
      <div className="grid grid-cols-[1fr_1fr] gap-[24px] pr-[32px] pl-[32px] pb-[96px]">
        <section>
          <img
            src={images[0].src}
            alt={images[0].alt}
            className="object-cover cursor-pointer transition-transform duration-500 hover:-translate-y-[10px]"
          />
        </section>
        <section className="grid grid-rows-[1fr_1fr] gap-[24px] ">
          <img
            src={images[1].src}
            alt={images[1].alt}
            className="object-cover cursor-pointer transition-transform duration-500 hover:-translate-y-[10px]"
          />
          <div className="grid grid-cols-[1fr_1fr] gap-[24px]">
            <img
              src={images[2].src}
              alt={images[2].alt}
              className="object-cover cursor-pointer transition-transform duration-500 hover:-translate-y-[10px]"
            />
            <img
              src={images[3].src}
              alt={images[3].alt}
              className="object-cover cursor-pointer transition-transform duration-500 hover:-translate-y-[10px]"
            />
          </div>
        </section>
      </div>
    </div>
  );
}
export default Curated;
