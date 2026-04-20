function Fluid() {
    return (
      <div className="grid grid-cols-2 gap-[64px]  mt-[96px] mb-[96px] px-[32px]">
        <section className="w-[576px] flex flex-col gap-[16px] ">
          <p className="text-[48px] leading-[48px] tracking-[-2.4px] text-[#131B2E]">
            Stay Fluid.
          </p>
          <p className="text-[18px] leading-[29.25px] text-[#434656]">
            Join our inner circle for early access to limited edition drops,
            architectural insights, and member-only pricing.
          </p>
        </section>
        <section>
          <div className="grid grid-cols-[2fr_1fr] gap-[16px] w-[576px]">
            <input
              type="text"
              placeholder="Enter your email"
              className=" h-[58px] rounded-[12px] border-[#C4C5D933] border-[1px] px-[16px] py-[12px] bg-[#F2F3FF]"
            />
            <button className="bg-[#131B2E]  rounded-[12px] h-[58px]  cursor-pointer hover:bg-[#3132ED] transition duration-300">
              <span className="font-bold text-[16px] leading-[24px] text-[#FAF8FF] ">
                {" "}
                Subscribe
              </span>
            </button>
            <div className="text-[12px] leading-[16px] text-[#43465699] pl-[8px]">
              By subscribing, you agree to our Privacy Policy and Terms of
              Service.
            </div>
          </div>
        </section>
      </div>
    );
}
export default Fluid;
