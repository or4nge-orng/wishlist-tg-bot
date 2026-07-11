import SwiftUI

enum AppTheme {
    static let accent = Color("AccentColor")
    static let accentLight = Color(red: 0.98, green: 0.85, blue: 0.88)
    static let background = Color(red: 0.98, green: 0.96, blue: 0.97)
    static let cardBackground = Color.white
    static let secondaryText = Color(red: 0.45, green: 0.42, blue: 0.44)
    static let gradient = LinearGradient(
        colors: [
            Color(red: 0.91, green: 0.30, blue: 0.44),
            Color(red: 0.75, green: 0.25, blue: 0.55)
        ],
        startPoint: .topLeading,
        endPoint: .bottomTrailing
    )
}

struct PrimaryButtonStyle: ButtonStyle {
    var isDisabled: Bool = false

    func makeBody(configuration: Configuration) -> some View {
        configuration.label
            .font(.headline)
            .foregroundStyle(.white)
            .frame(maxWidth: .infinity)
            .padding(.vertical, 16)
            .background(
                RoundedRectangle(cornerRadius: 14)
                    .fill(isDisabled ? Color.gray.opacity(0.4) : AppTheme.accent)
            )
            .scaleEffect(configuration.isPressed ? 0.97 : 1)
            .animation(.easeInOut(duration: 0.15), value: configuration.isPressed)
    }
}

struct SecondaryButtonStyle: ButtonStyle {
    func makeBody(configuration: Configuration) -> some View {
        configuration.label
            .font(.headline)
            .foregroundStyle(AppTheme.accent)
            .frame(maxWidth: .infinity)
            .padding(.vertical, 16)
            .background(
                RoundedRectangle(cornerRadius: 14)
                    .stroke(AppTheme.accent, lineWidth: 1.5)
            )
            .scaleEffect(configuration.isPressed ? 0.97 : 1)
    }
}

struct CardModifier: ViewModifier {
    func body(content: Content) -> some View {
        content
            .padding()
            .background(AppTheme.cardBackground)
            .clipShape(RoundedRectangle(cornerRadius: 16))
            .shadow(color: .black.opacity(0.06), radius: 8, y: 4)
    }
}

extension View {
    func cardStyle() -> some View {
        modifier(CardModifier())
    }
}
