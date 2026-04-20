import icon from "../../assets/Comma.png";
import quotter from "../../assets/Quotter.png";
function Quote() {
  return (
    <div className="bg-[#EAEDFF]  h-[558px] py-[96px] px-[192px ] flex   flex-col items-center ">
      <img src={icon} alt="Quote" className="w-[42.5px] h-[30px]" />
      <p className="w-[866.8900146484375px] h-[200px] text-[36px] font-bold leading-[40px] italic text-[#131B2E] text-center mt-[40px] ">
        "The shopping experience here feels like walking through a contemporary
        art gallery. The attention to detail in both the interface and the
        products they curate is unparalleled in modern e-commerce."
      </p>
      <div className="flex flex-row mt-[40px] gap-[24px] items-center">
        <section>
          <img
            src={quotter}
            alt="Quotter"
            className="rounded-full border-[#3132ED] border-[2px] object-cover]"
          />
        </section>
        <div className="flex flex-col">
          <p className="font-black leading-[24px] text-[#131B2E] text-[18px]font- Inter">
            Julian Vance
          </p>
          <p className="font-medium text-[14px] leading-[20px] text-[#434656] ">
            Creative Director, NeoSpace
          </p>
        </div>
      </div>
    </div>
  );
}
export default Quote;
