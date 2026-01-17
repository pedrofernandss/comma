FROM eclipse-temurin:17-jdk-alpine AS build-stage

# Create non-root user
RUN addgroup -S commagroup; adduser --ingroup commagroup --disabled-password comma
USER comma

# Create folder
WORKDIR /app
# Copy the application files
COPY ./src/main ./src/main
# Copy the gradle build file
COPY build.gradle settings.gradle gradlew ./
COPY gradle ./gradle
# Build the project
RUN ./gradlew bootJar

FROM eclipse-temurin:17-jre-alpine AS run-stage

# Copy the genareted executable file from the previous step/stage
COPY --from=build-stage /app/build/libs/*jar app.jar

# Execute the .jar file
ENTRYPOINT ["java", "-jar", "app.jar"]