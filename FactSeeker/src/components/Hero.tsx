import { Button } from "@/components/ui/button";
import { ShieldCheck, AlertTriangle, Zap } from "lucide-react";
import heroBg from "@/assets/hero-bg.jpg";

const Hero = () => {
  return (
    <section className="relative min-h-screen flex items-center justify-center overflow-hidden">
      {/* Background Image */}
      <div 
        className="absolute inset-0 bg-cover bg-center bg-no-repeat opacity-20"
        style={{ backgroundImage: `url(${heroBg})` }}
      />
      
      {/* Gradient Overlay */}
      <div className="absolute inset-0 bg-gradient-hero" />
      
      {/* Animated Elements */}
      <div className="absolute inset-0 overflow-hidden pointer-events-none">
        <div className="absolute top-1/4 left-1/4 w-96 h-96 bg-primary/10 rounded-full blur-3xl animate-pulse-glow" />
        <div className="absolute bottom-1/4 right-1/4 w-96 h-96 bg-secondary/10 rounded-full blur-3xl animate-pulse-glow delay-1000" />
      </div>

      {/* Content */}
      <div className="relative z-10 container mx-auto px-4 py-20">
        <div className="max-w-4xl mx-auto text-center space-y-8 animate-slide-up">
          {/* Badge */}
          <div className="inline-flex items-center gap-2 px-4 py-2 bg-gradient-card backdrop-blur-sm rounded-full border border-primary/20 shadow-glow">
            <ShieldCheck className="w-5 h-5 text-primary" />
            <span className="text-sm font-medium text-foreground">AI-Powered Fact Verification</span>
          </div>

          {/* Heading */}
          <h1 className="text-5xl md:text-7xl font-bold text-foreground leading-tight">
            FactSeeker
            <span className="block bg-gradient-primary bg-clip-text text-transparent mt-2">
              Detect. Verify. Alert.
            </span>
          </h1>

          {/* Subheading */}
          <p className="text-xl md:text-2xl text-muted-foreground max-w-3xl mx-auto">
            Advanced multimodal AI system protecting society from misinformation through autonomous detection, 
            real-time verification, and instant public alerts.
          </p>

          {/* Stats */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 max-w-3xl mx-auto pt-8">
            <div className="bg-gradient-card backdrop-blur-sm p-6 rounded-xl border border-primary/10 shadow-lg">
              <div className="text-3xl font-bold text-primary">99.2%</div>
              <div className="text-sm text-muted-foreground mt-1">Detection Accuracy</div>
            </div>
            <div className="bg-gradient-card backdrop-blur-sm p-6 rounded-xl border border-secondary/10 shadow-lg">
              <div className="text-3xl font-bold text-secondary">Real-Time</div>
              <div className="text-sm text-muted-foreground mt-1">Verification Speed</div>
            </div>
            <div className="bg-gradient-card backdrop-blur-sm p-6 rounded-xl border border-success/10 shadow-lg">
              <div className="text-3xl font-bold text-success">Multi-Modal</div>
              <div className="text-sm text-muted-foreground mt-1">Content Analysis</div>
            </div>
          </div>

          {/* CTA Buttons */}
          <div className="flex flex-col sm:flex-row items-center justify-center gap-4 pt-8">
            <Button variant="hero" size="lg" className="gap-2">
              <Zap className="w-5 h-5" />
              Try Demo
            </Button>
            <Button variant="outline" size="lg">
              Learn More
            </Button>
          </div>

          {/* Trust Indicators */}
          <div className="flex flex-wrap items-center justify-center gap-8 pt-12 text-sm text-muted-foreground">
            <div className="flex items-center gap-2">
              <ShieldCheck className="w-4 h-4 text-success" />
              <span>Multi-Agent AI</span>
            </div>
            <div className="flex items-center gap-2">
              <AlertTriangle className="w-4 h-4 text-warning" />
              <span>RAG Verification</span>
            </div>
            <div className="flex items-center gap-2">
              <Zap className="w-4 h-4 text-primary" />
              <span>Autonomous Alerts</span>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Hero;
